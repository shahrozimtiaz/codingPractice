alert("Hello World");
document.write("Welcome:) <br>");
var vistorAge = prompt("What is your age?");

document.write("You're " + vistorAge + " years old. <br>");

if(parseInt(vistorAge) == 20){
	document.write("Cool! we're the same age. <br>")
}
else if(parseInt(vistorAge) < 20){
	document.write("Cool! you're younger than me. <br>")
}
else{
	document.write("Cool! you're older than me. <br>")
}
var hotText = 'Youtube tutorial on JavaScript'
var URL = "https://www.youtube.com/watch?v=48rz8udZBmQ"

document.write("Click to view " + hotText.link(URL))