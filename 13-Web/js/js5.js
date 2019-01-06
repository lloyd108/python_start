console.log("js5.js loaded...");


window.onload = function() {
	console.log("HTML load successful!")
};

writeTime = function(id) {
	var myDate = new Date();
	var myTime = myDate.toLocaleTimeString();
	var myDev = document.getElementById(id);
	// myDev.innerHTML = myTime;
	myDev.innerHTML = myDate;

	console.log(myDate, myTime);
};

plus = function(id) {
	console.log(arguments);
	var myDev = document.getElementById(id);
	// for(var i = 1; i <= 1000; i++){
	// 	myDev.style.width = i + 'px';
	// 	myDev.style.height = i + 'px';
	//
	// 	console.log(i+'px');
	// };
	var i = 0;
	var plusInterval = setInterval(function(){
		i++;
		myDev.style.width = i + 'px';
		myDev.style.height = i + 'px';
		myDev.style.lineHeight= i + 'px';
		myDev.style.textAlign = 'center';
		console.log(i + 'px');
		console.log(arguments);
		if(i == 300){
			clearInterval(plusInterval);
		}
	}, 200);
};
