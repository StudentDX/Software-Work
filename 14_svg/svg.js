//David Xiedeng & Pratham Rawat
//SoftDev1 pd1
//Ask Circles [Change || Die] While Moving, etc.
//2020-04-01

var pic = document.getElementById("vimage"); //svg
var clear = document.getElementById("clear"); //clearbutton
let moveButton = document.getElementById("moveButton");
let xtraButton = document.getElementById("xtraButton");
let children = []; // list of circles
let isMoving = false;
let isXtra = false;

// clearing
clear.addEventListener('click', e => {
  pic.innerHTML = ""
})

//drawing functions

// draw circle
function drawCircle(xcor, ycor){
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", xcor);
  c.setAttribute("cy", ycor);
  c.setAttribute("r", 10);
  c.setAttribute("fill", "blue");
  c.setAttribute("stroke", "blue");

  pic.appendChild(c);
  // Child, X-Speed Multiplier, Y-Speed Multiplier; retrieved from Pratham
  children.push([c, Math.random() < 0.5 ? -1 : 1, Math.random() < 0.5 ? -1 : 1])

  c.addEventListener('click', e => {
    changeColor(c);
  });
  return c;
}

// general function
// used in killCircle, and <animate function>
function moveCircle(circle, xcor, ycor){
  circle.remove();
  drawCircle(xcor, ycor);
}

// called on cyan circle
// move circle
function killCircle(circle){
  var x = Math.floor(Math.random() * 500);
  var y = Math.floor(Math.random() * 500);
  //drawing new circle
  moveCircle(circle,x,y)
}

// called on blue circle
// takes circle element
// circle change color
// circle gets new listener
function changeColor(circle){
  circle.setAttribute("fill", "cyan");
  circle.setAttribute("stroke", "cyan");
  // removes listener on circle for this function
  circle.removeEventListener('click', changeColor)
  circle.addEventListener('click', e => {
    killCircle(circle);
  });
};

// initial event listener on svg
pic.addEventListener('click', e => {
  var x = e.offsetX;
  var y = e.offsetY;
  // checks to only draw when clicking blank space
  if (e.target == pic) {
    circle = drawCircle(x,y);
  }
});

var currentFrame;

// animating start
moveButton.addEventListener("click", function(e) {
  isMoving = !isMoving;
  // prevents animation speed doubling
  window.cancelAnimationFrame(currentFrame);
  animate();
});

xtraButton.addEventListener('click', function(e) {
  isXtra = !isXtra;
  window.cancelAnimationFrame(currentFrame);
  animate();
});

var rgb = [0,0,0];

// animating function; retrieved from Pratham
let animate = () => {
  if(!(isMoving || isXtra)) {
    cancelAnimationFrame(currentFrame);
    return "animation stopped"
  }
  for(i = 0; i < children.length; i++) {
    // moves circle based on coord deltas in array child
    // speed multiplier changed to 1
    if(isMoving) {
      children[i][0].setAttribute("cx", parseInt(children[i][0].getAttribute("cx"), 10) + (1 * children[i][1]))
      children[i][0].setAttribute("cy", parseInt(children[i][0].getAttribute("cy"), 10) + (1 * children[i][2]))
      // reverses delta when border reached
      if(children[i][0].getAttribute("cx") > 500 || children[i][0].getAttribute("cx") < 0) {
        children[i][1] = -children[i][1];
      }
      if(children[i][0].getAttribute("cy") > 500 || children[i][0].getAttribute("cy") < 0) {
        children[i][2] = -children[i][2];
      }
    }
    if (isXtra){
      let test = 1;
      // changes color of circles circles through hexcode
      children[i][0].setAttribute("fill", `rgb(${rgb[0]},${rgb[1]},${rgb[2]})`);
      children[i][0].setAttribute("stroke", `rgb(${rgb[0]},${rgb[1]},${rgb[2]})`);
      //console.log(children[i][0].fill)
      // increases rbg values
      if (rgb[0] < 255) {
        rgb[0] += 1;
      }
      else if (rgb[1] < 255) {
        rgb[1] += 1;
      }
      else if (rgb[2] < 255) {
        rgb[2] += 1;
      }
      else {
        rgb = [0,0,0];
      }
    }
  }
  currentFrame = window.requestAnimationFrame(animate);
}
