//generates the body grid
gridGenerator();

//it just creates div elements nested in the div with the grid ID
//a 2D field with x and y hardcoded to 11, it's the upper limit of turtlesim's
//turtle's field
function gridGenerator() {
    var container = document.getElementById("grid");
    for (let i = 0; i < 11; i++) {
        let row = document.createElement("div");
        row.className = "row";
        container.appendChild(row);
        for (let j = 0; j <= 11; j++) {
            let cell = document.createElement("div");
            cell.className = "col gridsquare m-1";
            cell.id = `${j}:${i}`;
            row.appendChild(cell);
        }
    }
}