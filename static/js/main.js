
var colorChange;
var initialColor = "#000000";

window.addEventListener("load", changemycolor);

function changemycolor() {
colorChange = document.querySelector("#colorChange");
colorChange.value = initialColor;
colorChange.addEventListener("input", update);
}

function update(event) {
document.getElementById('colorbox').style.backgroundColor = event.target.value;
document.getElementById('HexValue').innerHTML = event.target.value;
}


