var changeHeading = function(e) {
	var h = document.getElementById("h");
	h.innerHTML = e;
	console.log(e);
};


var removeItem = function(e) {
	e.remove();
};


const lis = document.getElementsByTagName("li");

for (let i = 0; i < lis.length; i++) {
	let item = lis[i];
	item.addEventListener("mouseover", () => {
		changeHeading(item.innerHTML);
		//console.log(i);
	});
	//console.log(lis[i]);
	item.addEventListener("mouseout", () => {changeHeading("Hello World")});
	item.addEventListener("click", () => {removeItem (item)});
};

/*
var addItem = function(e) {
	var list = ;
	var item = document.createElement;
	??? = "WORD";
	???
	list.???(item);
};

var button = document.getElementById("b")
*/
