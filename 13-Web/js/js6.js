var myObj1 = new Object();
myObj1.name = 'yz';
myObj1.age = 32;
myObj1.gender = 'male';
myObj1.say = function(){
  alert("I'm saying...");
};

var myObj2 = {
  name: 'zfb',
  age: 29,
  gender: 'female',
  say: function(){
    alert("Keke...");
  }
};

myObj2.height = '180cm';

function myObj(name, age, gender){
  this.name = name;
  this.age = age;
  this.gender = gender;
  this.say = function(){
    alert("new type..." + name + age + gender);
  }
  console.log(this);
};

var myObj3 = new myObj('obj3', 22, 'unknown');
myObj3.say();
for(i in myObj3){
  console.log(i, myObj3[i]);
};
console.log(myObj3.constructor);

var changeContent = function(id, content){
  var myDiv = document.getElementById(id);
  if(content == undefined){
    myDiv.innerHTML = myObj1.name + myObj1.age + myObj1.gender + myObj2.height;
    myObj1.say();
  }
  // console.log(id, content);
  // console.log(myObj1.content);
  // myDiv.innerHTML = myObj1.'content';
}
