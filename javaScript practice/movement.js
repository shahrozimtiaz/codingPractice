window.onload = function () {
    canv = document.getElementById("gc");
    ctx = canv.getContext("2d");
    document.addEventListener("keydown",keydown);
    document.addEventListener("keyup",keyup);
    images = ["knightr1.png","knightr2.png","knightr3.png","knightr4.png","knightr5.png","knightr6.png"]
    move();
}
var map = [];
player = [50,180];
counter=0;
function move(){
    if(map[37]) {
        player[0] -= 10;
        if (counter > 0) {
            counter--;
        } else {
            counter = 5;
        }
        image = new Image();
        image.src = images[counter];
        image.onload = () => {
            ctx.fillStyle="white";
            ctx.fillRect(0,0,canv.width,180+250);
            ctx.fillStyle="black";
            ctx.fillRect(0,300,canv.width,canv.height);
            ctx.drawImage(image, player[0], player[1], 60, 250);
        }
    }else if(map[39]) {
        player[0] += 10;
        if (counter < 5) {
            counter++;
        } else {
            counter = 0;
        }
        image = new Image();
        image.src = images[counter];
        image.onload = () => {
            ctx.fillStyle="white";
            ctx.fillRect(0,0,canv.width,180+238);
            ctx.fillStyle="black";
            ctx.fillRect(0,300,canv.width,canv.height);
            ctx.drawImage(image, player[0], player[1], 60, 250);
        }
    }else{
        image = new Image();
        image.src = images[counter];
        // image.src="knightr4.png";
        image.onload = () => {
            ctx.fillStyle="white";
            ctx.fillRect(0,0,canv.width,180+238);
            ctx.fillStyle="black";
            ctx.fillRect(0,300,canv.width,canv.height);
            ctx.drawImage(image, player[0], player[1], 60, 250);
        }
    }
    window.requestAnimationFrame(move);
}
function keydown(event){
    map[event.which]=true;
}
function keyup(event){
    map[event.which]=false;
    counter = 0;
}