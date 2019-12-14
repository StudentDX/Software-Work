//David Xiedeng
//SoftDev1 pd1
//K27 -- Sequential Progression
//2019-12-13 

var helloworld = function() {
	console.log("hello world");
};

var fact = function(n) {
	if (n < 2){
		return 1;
	}
	else{
		return n = n * (fact(n - 1));
	}
};

var fibonacci = function(n,a=0,b=1) {
	while (n > 1){
		c = a;
		a = b;
		b = c+b;
		n-=1;
	}
	return a;
};

var gcd = function(x,y){
	r = x % y;
	while (r != 0){
		x = y;
		y = r;
		r = x % y;
	}
	return y;
}

var students = ["Alice","Bob","Charlie","Devin","Elsa", "Fred", "George"];

var randomStudent = function(){
	i = Math.floor(Math.random() * students.length)
	return students[i];
}

var input = [4,2];

var changeAnswer = (ans) => {
    ansDiv = document.getElementById("answer");
    ansDiv.innerHTML = (ans);
}

var factButton = document.getElementById("fact");
factButton.addEventListener('click', () => {
    ans = fact (input[0]);
    console.log(ans);
    changeAnswer(ans);
    });

var fibButton = document.getElementById("fib");
fibButton.addEventListener('click', () => 
    {
        ans = fibonacci (input[0]);
        console.log(ans);
        changeAnswer(ans);
    }
);

/*
var GCDButton = document.getElementById("gcd");
GCDButton.addEventListener('click', () =>
*/