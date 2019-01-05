alert('js4.js is imported...')

window.onload = function() {
	var myDev1 = document.getElementById('item1');
	console.log(myDev1, typeof(myDev1));

	// myDev1.style.color="red";
	userInput = document.getElementById("uname")
	console.log(userInput)
};

setRed = function(id){
	var myDev2 = document.getElementById(id);
	myDev2.style.color="red";
	myDev2.style.width="500px";

	console.log(myDev2.innerHTML)
	myDev2.innerHTML="666666666666666666666"
	myDev2.style.backgroundColor="yellow"
};

setBlack = function(id){
	var myDev2 = document.getElementById(id);
	myDev2.style.color="black";
	myDev2.style.width="200px";

	console.log(myDev2.innerHTML)
	myDev2.innerHTML="black"

	console.log(myDev2.style.width)
};

