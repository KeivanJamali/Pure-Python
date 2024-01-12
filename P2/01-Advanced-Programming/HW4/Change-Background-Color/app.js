let red = document.getElementById("red");
let yellow = document.getElementById("yellow");

let green = document.getElementById("green");
let blue = document.getElementById("blue");

let orange = document.getElementById("orange");
let pink = document.getElementById("pink");
function paint(color) {
    document.body.style.backgroundColor = color;}
red.addEventListener("click", () => {
    paint("red");});
yellow.addEventListener("click", () => {
    paint("yellow");});
green.addEventListener("click", () => {
    paint("green");});
blue.addEventListener("click", () => {
    paint('blue');});
orange.addEventListener('"click"', () => {
    paint('orange');});
pink.addEventListener("click", () => {
    paint('pink');});



