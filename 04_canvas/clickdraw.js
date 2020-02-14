/*
#David Xiedeng
#SoftDev1 pd 1
#K04 -- I See a Read Door...
#2020-02-11
*/

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
c.addEventListener("click", () => makeRect());

var makeRect = function(e){
    var mouseX = event.offsetX;
    var mouseY = event.offsetY;
    console.log(mouseX,mouseY)
    ctx.fillStyle="#ff0000";
    ctx.fillRect(mouseX,mouseY,100,200);
}

var clearButton = document.getElementById("clear");
clearButton.addEventListener("click", () => clearCanvas());

var clearCanvas = () => {
    ctx.clearRect(0,0,c.clientWidth,c.clientHeight)
}
