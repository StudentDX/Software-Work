/*
Manfred Tan, David Xiedeng
SoftDev1 pd1
K #07: They lock us in the tower whenever we get caught
2020-02-12
*/

var c = document.getElementById("playground")
var ctx = c.getContext("2d")
ctx.fillStyle = "#8a28e6"

var running = false;
var radius = 0;
var expand = true;
var id = 0;

var grow = function(e) {
    id = window.requestAnimationFrame(grow);
    if (expand) {
        radius += 1;
        if (radius==300) expand=false;
    }
    else {
        radius -= 1;
        if (radius==0) expand=true;
    }
    console.log(radius,expand);
    ctx.clearRect(0,0,600,600);
    ctx.beginPath();
    ctx.arc(300,300, radius, 0, Math.PI * 2, true);
    ctx.fill();
    ctx.closePath();
}

var changeX = 1;
var changeY = 1;
var valueX = 0;
var valueY = 0;

var move = function(e) {
    id = window.requestAnimationFrame(move);
    ctx.clearRect(0,0,600,600);
    ctx.beginPath();
    ctx.drawImage(logo, valueX, valueY, 50, 50);
    //ctx.arc(valueX,valueY,5, 0, Math.PI * 2, true);
    ctx.fill();
    ctx.closePath();
    if (valueX >= 575 || valueX <= 25) changeX *= -1;
    if (valueY >= 575 || valueY <= 25) changeY *= -1;
    valueX += changeX;
    valueY += changeY;
    console.log(valueX, changeX, valueY, changeY)
}

var animate = function(e) {
    window.cancelAnimationFrame(id);
    console.log('ANIMATE')
    grow();
};

var logo = new Image();
logo.src = "logo.png"

var bounce = function(e) {
    window.cancelAnimationFrame(id);
    console.log('BOUNCE')

    changeX = 1;
    changeY = 1;
    valueX = Math.floor(Math.random() * 550) + 25;
    valueY = Math.floor(Math.random() * 550) + 25;
    move();
}

var pause = function(e) {
    window.cancelAnimationFrame(id);
};


var start = document.getElementById("start");
start.addEventListener('click', animate);


var stop = document.getElementById("stop");
stop.addEventListener('click', pause);

var dvd = document.getElementById("dvd");
dvd.addEventListener('click', bounce);
