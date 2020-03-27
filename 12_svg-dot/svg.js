var pic = document.getElementById("vimage");

var prevX;
var prevY;

pic.addEventListener('click', e => {
	// create circle
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
	var x = e.offsetX;
  var y = e.offsetY;
  c.setAttribute("cx", x);
  c.setAttribute("cy", y);
  c.setAttribute("r", 10);
  c.setAttribute("fill", "black");
  c.setAttribute("stroke", "black");
  pic.appendChild(c);

  //create line connecting circle
  if (prevX != null) {
  	var line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", prevX);
  	line.setAttribute("y1", prevY);
  	line.setAttribute("x2", x);
  	line.setAttribute("y2", y);
  	line.setAttribute("stroke", "black");
    pic.appendChild(line);
  }
  prevX = x;
  prevY = y;


});
