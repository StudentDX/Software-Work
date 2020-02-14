// Nice - Henry Liu & David Xiedeng
// SoftDev1 pd1
// K06 -- Dot dot dot
// 2020-02-07

var c = document.getElementById("slate")
var ctx = c.getContext("2d");
document.getElementById("clear").addEventListener("click", (e) => {
    ctx.fillStyle = "#fff";
    ctx.fillRect(0, 0, c.width, c.height);
    ctx.closePath();
    start = true;
});

var start = true;


c.addEventListener("click", (e) => {
    // Offset gives the (x, y) coordinate relative to the top left corner of the element clicked on
    var x = e.offsetX;
    var y = e.offsetY;
    if (start){
      start=false;
      ctx.beginPath();
    }
    ctx.fillStyle = "blue";
    ctx.lineTo(x,y);
    ctx.stroke();
    /*
    ctx.arc(x, y, 5, 0, 2 * Math.PI);
    */

});
