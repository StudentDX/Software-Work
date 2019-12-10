var helloworld = function() {
	return("hello world");
};

var fact = function(n) {
	if (n < 2){
		return 1;
	}
	else{
		return n = n * (fact(n - 1));
	}
};

var test = fact(4);
