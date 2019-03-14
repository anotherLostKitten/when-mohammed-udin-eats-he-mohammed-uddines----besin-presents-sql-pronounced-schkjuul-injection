console.log("hello????");

var sl=document.getElementById("slide_location");
var pl=document.getElementById("pres_left");
var pr=document.getElementById("pres_right");
var p=document.getElementById("pres");


var slideLen=2


var pi=sl.getElement("value");
console.log(pi);

var slideu = ()=>{
	sl.setattribute("slide_location",pi);
	p.setAttribute("src","static/slide"+pi+".png");
};

pl.addEventListener("click",(e)=>{
	if(pi>0)
		pi--;
	slideu();
});
pr.addEventListener("click",(e)=>{
	if(pi<slideLen-2)
		pi++;
	slide();
});
