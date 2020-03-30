//David Xiedeng & Henry Liu
//SoftDev1 pd1
//K13 -- SVG
//2020-03-30

// clearing
var clear = document.getElementById("clear")
clear.addEventListener('click', e => {
  pic.innerHTML = null
})

//drawing functions
var pic = document.getElementById("vimage");

// draw circle
function drawCircle(xcor, ycor){
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", xcor);
  c.setAttribute("cy", ycor);
  c.setAttribute("r", 10);
  c.setAttribute("fill", "blue");
  c.setAttribute("stroke", "blue");
  pic.appendChild(c);
	c.addEventListener('click', e => {
		changeColor(c);
	});
  return c;
}

// move circle
function moveCircle(circle){
		// removing original circle
		circle.remove();
		var x = Math.floor(Math.random() * 500);
		var y = Math.floor(Math.random() * 500);

		drawCircle(x, y);
		console.log("move turn");
		}


//takes element circle
// circle change color
function changeColor(circle){
    circle.setAttribute("fill", "cyan");
    circle.setAttribute("stroke", "cyan");
    circle.removeEventListener('click', changeColor)
		circle.addEventListener('click', e => {
			moveCircle(circle);
		});
		console.log("circle turn");
    };

pic.addEventListener('click', e => {
  var x = e.offsetX;
  var y = e.offsetY;
  circle = drawCircle(x,y);
	console.log("pic turn");

  });
