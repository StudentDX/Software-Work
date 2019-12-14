var changeHeading = function(e) {
	var h = document.getElementById("h");
	h.innerHTML = e;
	console.log(e);
};


var removeItem = function(e) {
	e.remove();
};


const lis = document.getElementsByTagName("li");


var makeDeletable = (item) => {
    item.addEventListener("mouseover", () => {
		changeHeading(item.innerHTML);
	});
	item.addEventListener("mouseout", () => {changeHeading("Hello World")});
	item.addEventListener("click", () => {removeItem (item)});
}

for (let i = 0; i < lis.length; i++) {
	let item = lis[i];
	makeDeletable(item);
};


var addItem = function(e) {
	var list = document.getElementsByTagName("ol")[0];
	var item = document.createElement("li");
	item.innerHTML = "WORD";
	makeDeletable(item);
	list.appendChild(item);
};

var button = document.getElementById("b")
button.addEventListener('click', addItem)

var fib = function(n) {
	if (n < 2) {
		return 1;
	}
	else {
		return fib(n-1)+fib(n-2);
	}
};

var addFib = function (e) {
	var list = document.getElementsByTagName("ol")[1];
	var n = list[-1].innerHTML;
	console.log(n)
}

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
