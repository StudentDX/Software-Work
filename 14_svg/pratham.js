// Eric Lau and Pratham Rawat
// SoftDev2 pd1
// K13 -- Ask Circles [Change || Die]
// 2020-03-31
let pic = document.getElementById("vimage");
let isMoving = false;
let isXtra = false;
let clearButton = document.getElementById("clear");
let moveButton = document.getElementById("moveButton");
let xtraButton = document.getElementById("xtraButton");
let children = []; // list of circles
let onCircle = false;

// creates circle when svg clicked
pic.addEventListener("mouseup", (e) => {
  if (!onCircle) {
    addCircle(e.offsetX, e.offsetY);
  }
  onCircle = false;
});

// function to create circle
let addCircle = (x, y) => {
  let c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", x);
  c.setAttribute("cy", y);
  c.setAttribute("r", "15");
  c.setAttribute("fill", "blue");
  c.setAttribute("stroke", "blue");
  // Child, X-Speed Multiplier, Y-Speed Multiplier
  children.push([c, Math.random() < 0.5 ? -1 : 1, Math.random() < 0.5 ? -1 : 1])
  pic.appendChild(c);
  c.addEventListener("mousedown", () => { onCircleClick(c) });
}

// click on a circle
let onCircleClick = (c) => {
  onCircle = true;
  //checks color of circle
  if (c.getAttribute("fill") == "blue") {
    // changes color of circle
    console.log("type blue");
    c.setAttribute("fill", "cyan");
    c.setAttribute("stroke", "cyan");
  } else if (c.getAttribute("fill") == "cyan") {
    // creates new circle
    pic.removeChild(c);
    addCircle(Math.random() * 500, Math.random() * 500);
  }
}

// clears svg content
//iterates through out children to remove
clearButton.addEventListener("click", function (e) {
  let fc = pic.firstChild;
  while (fc) {
    pic.removeChild(fc);
    fc = pic.firstChild;
  }
});

// animating start
moveButton.addEventListener("click", function(e) {
  console.log("moov");
  isMoving = !isMoving;
  isXtra = false;
  if(isMoving) {
    window.requestAnimationFrame(animate);
  } else {
    window.cancelAnimationFrame();
  }
});

// animating function
let animate = () => {
  console.log("k");
  for(i = 0; i < children.length; i++) {
    children[i][0].setAttribute("cx", parseInt(children[i][0].getAttribute("cx"), 10) + (5 * children[i][1]))
    children[i][0].setAttribute("cy", parseInt(children[i][0].getAttribute("cy"), 10) + (5 * children[i][2]))
    if(children[i][0].getAttribute("cx") > 500 || children[i][0].getAttribute("cx") < 0) {
      children[i][1] = -children[i][1];
    }
    if(children[i][0].getAttribute("cy") > 500 || children[i][0].getAttribute("cy") < 0) {
      children[i][2] = -children[i][2];
    }
  }
  currentFrame = window.requestAnimationFrame(animate);
}
