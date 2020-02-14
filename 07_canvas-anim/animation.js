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

var animate = function(e) {
    if (!running) {
        running = true;
        console.log('workd')
        grow();
    };
};

var pause = function(e) {
    window.cancelAnimationFrame(id);
    running = false
};



var start = document.getElementById("start");
start.addEventListener('click', animate);


var stop = document.getElementById("stop");
stop.addEventListener('click', pause);
