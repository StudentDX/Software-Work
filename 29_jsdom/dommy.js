var changeHeading = function(e) {
	var h = document.getElementById("h");
	h.innerHTML = e;
	console.log(e);
};

/*
var removeItem = function(e) {

};
*/

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
	var html = lis[i].innerHTML;
	console.log(i);
	console.log(lis[i]);
	console.log(html);
	lis[i].addEventListener("mouseover", () => {changeHeading (html)});
	lis[i].addEventListener("mouseout", () => {changeHeading ("Hello World!")});
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
