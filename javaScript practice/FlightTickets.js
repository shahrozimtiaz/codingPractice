var body;
var button;
window.onload = function () {
    canv = document.getElementById("gc");
    ctx = canv.getContext("2d");
    images = ["knightr1.png","knightr2.png","knightr3.png","knightr4.png","knightr5.png","knightr6.png"]
    button = document.createElement("button");
    button.innerHTML = "Book a Flight";
    button.addEventListener ("click", clicked);
    body = document.getElementsByTagName("body")[0];

    button.style.width = '200px'; // setting the width to 200px
    // button.style.height = '200px'; // setting the height to 200px
    button.style.background = 'teal'; // setting the background color to teal
    button.style.color = 'white'; // setting the color to white
    button.style.fontSize = '20px'; // setting the font size to 20px
    body.appendChild(button);
    id = requestAnimationFrame(loop);

};
tickets = 4;
function loop(){
    ctx.fillStyle = "white";
    ctx.fillRect(0,0,canv.width,canv.height);
    ctx.fillStyle= "black";
    ctx.font = "44px Georgia";
    ctx.fillText("Tickets left: " + tickets, 0, 200);
    if(tickets == 0){
        alert("Sorry, no more tickets.")
        cancelAnimationFrame(id);
    }
    requestAnimationFrame(loop);
}

function clicked() {
    tickets--;
}