/*
#David Xiedeng
#SoftDev1 pd 1
#K04 -- I See a Read Door...
#2020-02-11
*/

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
c.addEventListener("click", () => draw());

var makeRect = function(e){
    var mouseX = event.offsetX;
    var mouseY = event.offsetY;
    console.log(mouseX,mouseY)
    ctx.fillStyle="#ff0000";
    ctx.fillRect(mouseX,mouseY,100,200);
}

var makeCircle = function(e) {
  var mouseX = event.offsetX;
  var mouseY = event.offsetY;
  //code that draws circle
  ctx.beginPath();
  ctx.fillStyle="#ff0000";
  //     (x,y, radius, start angle, end angle)
  ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();
}

var draw = function(e) {
  if (currentDrawMode == 0){
    makeRect();
  }
  else {
    makeCircle();
  }
}

// 0 for rect mode, 1 for circle
var currentDrawMode = 0;

var toggleStyle = function(e) {
  if (currentDrawMode == 0) {
    toggleButton.innerHTML = "Circle";
    currentDrawMode = 1;
  }
  else {
    toggleButton.innerHTML = "Rectangle";
    currentDrawMode = 0;
  }
}

var toggleButton = document.getElementById("toggle");
toggleButton.addEventListener("click", () => toggleStyle());

var clearButton = document.getElementById("clear");
clearButton.addEventListener("click", () => clearCanvas());

var clearCanvas = () => {
    ctx.clearRect(0,0,c.clientWidth,c.clientHeight)
}
