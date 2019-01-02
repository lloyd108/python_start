alert('js4.js is imported...')

window.onload = function() {
	var myDev1 = document.getElementById('item1');
	console.log(myDev1, typeof(myDev1));

	// myDev1.style.color="red";
};

setRed = function(id){
	var myDev2 = document.getElementById(id);
	myDev2.style.color="red";
};
