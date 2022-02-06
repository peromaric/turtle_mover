//websocket logic here
const socketRosSubscriber = new WebSocket("ws:/localhost:9090");
const socketFastApi = new WebSocket("ws:/localhost:8888/turtle_ai_pose")
//cheesy stuff, figure out something better when you've time please
let last_turtle_element = document.createElement("div");
let last_turtle_ai_element = document.createElement("div");
last_turtle_element.className = "empty";
last_turtle_ai_element.className = "empty_ai"
let turtleAiScore = 0;
let turtleScore = 0;

socketRosSubscriber.onopen = async function (event) {
    alert("Connection established");
    alert("Contacting turtle...");
    socketRosSubscriber.send(JSON.stringify({ op: "subscribe", topic: "/turtlesim1/turtle1/pose" }));
};

socketFastApi.onopen = async function (event) {
    alert("Connection established");
    alert("Contacting ai turtle...");
    socketRosSubscriber.send("");
};

socketRosSubscriber.onmessage = function (event) {
    let msg = JSON.parse(event.data)["msg"];
    let x = parseInt(msg["x"]);
    let y = parseInt(msg["y"]);
    let pose = `${x}:${y}`;
    let element = document.getElementById(pose);
    if (element !== null) {
        if (last_turtle_element.id !== element.id) {
            if (last_turtle_element.className.includes("posed")) {
                last_turtle_element.classList.remove("posed");
                last_turtle_element.innerHTML = "";
            } else {
                if (element.classList.contains("food")) {
                    turtleScore ++;
                    document.getElementById("turtle-score").innerHTML = turtleScore
                    element.classList.remove("food");
                }
                last_turtle_element = null;
                last_turtle_element = element;
                last_turtle_element.classList.add("posed");
                last_turtle_element.innerHTML = "<img src='turtle.png' class='img-fit mx-auto d-block'> </img>"
            }
        }
    }

};

socketFastApi.onmessage = function (event) {
    let msg = JSON.parse(event.data)
    let x = parseInt(msg["x"]);
    let y = parseInt(msg["y"]);
    let pose_ai = `${x}:${y}`;
    let element = document.getElementById(pose_ai);
    if (element !== null) {
        if (last_turtle_ai_element.id !== element.id) {
            if (last_turtle_ai_element.className.includes("posed_ai")) {
                last_turtle_ai_element.classList.remove("posed_ai");
                last_turtle_ai_element.innerHTML = "";
            } else {
                if (element.classList.contains("food")) {
                    turtleScore ++;
                    document.getElementById("turtle-ai-score").innerHTML = turtleScore;
                    element.classList.remove("food");
                }
                last_turtle_ai_element = null;
                last_turtle_ai_element = element;
                last_turtle_ai_element.classList.add("posed_ai");
                last_turtle_ai_element.innerHTML = "<img src='turtleai.png' class='img-fit mx-auto d-block'> </img>"
            }
        }
    }

};

function socketClosure (event) {
    if (event.wasClean) {
        alert(`[close] Turtlenection successfully terminated`);
    } else {
        // e.g. server process killed or network down
        // event.code is usually 1006 in this case
        alert('[close] Connection died');
    }
}

socketRosSubscriber.onclose = function (event) {
    socketClosure(event)
}

socketFastApi.onclose = function (event) {
    socketClosure(event)
}

socketRosSubscriber.onerror = function (error) {
    alert(`Can't contact the turtle...`);
};

socketFastApi.onerror = function (error) {
    alert(`Can't contact the turtle...`);
};
