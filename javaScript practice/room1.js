window.onload=function(){
	canv=document.getElementById("gc");
	ctx=canv.getContext("2d");
	image = new Image();
	image.src="invader.jpg";
	document.addEventListener("keydown",keyPush);
	document.addEventListener("keyup",keyLift);
	timer = setInterval(game,100);
}
shooter = [180,380];
cannon = [shooter[0]+17,shooter[1]-8];
cannonBalls = [];
enemyCannonBalls = [];
invaders = [];
dir="";
fire=false;
enemyFire=false;
level=1;
score = 0;
lives = 3;
speed=[];
map=[];
balls=17;
function game(){
	ctx.fillStyle="white";
	ctx.fillRect(0,0,canv.width,canv.height);
}
function keyLift(event){
	map[event.keyCode]=false;
}