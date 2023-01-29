const item =
document.querySelector("div");

function changeColor() {

item.classList.toggle("red");
}
item.ondblclick =
changeColor;