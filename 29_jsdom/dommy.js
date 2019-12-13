var changeHeading = function(e) {
	var h = document.getElementById("h");
	h.innerHTML = e;
	console.log(e);
};

/*
var removeItem = function(e) {

};
*/

const lis = document.getElementsByTagName("li");

for (let i = 0; i < lis.length; i++) {
	let item = lis[i];
	item.addEventListener("mouseover", () => {
		changeHeading(item.innerHTML);
		//console.log(i);
	});
	//console.log(lis[i]);
	lis[i].addEventListener("mouseout", () => {changeHeading("Hello World")});
	//lis[i].addEventListener("click", removeItem);
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
