//get the food coordinates from the fastapi
let url = "http://localhost:8888/food_coords";
function getFoodCoords() {
    fetch(url).then(function (response) {
        return response.json();
    }).then(function (data) {
        let coords = parseFoodCoords(data);
        let foodElement = document.getElementById(coords);
        foodElement.classList.add("food")
        foodElement.innerHTML = "<img src='food.png' class='img-fit mx-auto d-block'> </img>"
    }).catch(function () {
        alert("Can't reach fastapi");
    });

    function parseFoodCoords(data) {
        return `${data["x"]}:${data["y"]}`;
    }
}