// Shahroz Imtiaz
// 1/9/2018
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
	ctx.fillStyle="black";
	ctx.fillRect(0,0,canv.width,canv.height);
	balls=17-cannonBalls.length;
	ctx.fillStyle="white";
	ctx.font = "14px Georgia";
	ctx.fillText("Score: " + score, 0, 11);
	ctx.fillText("Amno: " + balls, 0, 392);
	ctx.fillText("Lives: " + lives, 350, 11);
	ctx.fillText("Shahroz Imtiaz",285,392);
	ctx.font = "32px Georgia";
	ctx.fillText("Space Invaders",90,120);
	if(lives==0){//dead
		clearInterval(timer);
		alert("Game Over");
	}
	for(var i=0;i<invaders.length;i++){//invaders landed
		if(invaders[i][1]>=380){
			invaders.splice(j,1);
			lives--;
		}
	}
	for(var i=0;i<cannonBalls.length;i++){//shot invader
		for(var j=0;j<invaders.length;j++){
			if(((invaders[j][0]-5)+25)-cannonBalls[i][0]<=25 && ((invaders[j][0]-5)+25)-cannonBalls[i][0]>=0 && ((invaders[j][1]-5)+25)-cannonBalls[i][1]<=25 && ((invaders[j][1]-5)+25)-cannonBalls[i][1]>=0){
				ctx.fillStyle="black";
				ctx.fillRect(invaders[j][0],invaders[j][1],20,20);
				invaders.splice(j,1);
				speed.splice(j,1);
				cannonBalls.splice(i,1);
				score++;
				if(score%5==0){
					level++;
				}
			}
		}
	}
	for(var i=0;i<enemyCannonBalls.length;i++){//invader shot you
		if(((shooter[0]-5)+45)-enemyCannonBalls[i][0]<=45 && ((shooter[0]-5)+40)-enemyCannonBalls[i][0]>=0 && ((shooter[1]-5)+45)-enemyCannonBalls[i][1]<=45 && ((shooter[1]-5)+45)-enemyCannonBalls[i][1]>=0){
			lives--;
			enemyCannonBalls.splice(i,1);
		}
	}
	if(level==3){//level reset
		enemyFire = true;
		level=1;
	}
	for(var i=0;i<invaders.length;i++){//invader moves down
		ctx.fillStyle="black";
		ctx.fillRect(invaders[i][0],invaders[i][1],20,20);
		invaders[i][1]=invaders[i][1]+speed[i];
	}
	if(invaders.length < Math.random()*2){//create invader
		for(var i=1;i<=level;i++){
			invader();
			invader();
		}
	}
	for(var i=0;i<invaders.length;i++){//draw invader
		ctx.drawImage(image, invaders[i][0],invaders[i][1],20,20);
	}
	for(var i=0;i<cannonBalls.length;i++){//move cannonball up
		ctx.fillStyle="black";
		ctx.fillRect(cannonBalls[i][0],cannonBalls[i][1],5,5);
		cannonBalls[i][1]=cannonBalls[i][1]-6;
		if(cannonBalls[i][1]<0){
			cannonBalls.splice(i,1);
		}
	}
	for(var i=0;i<enemyCannonBalls.length;i++){//move enemy cannonball down
		ctx.fillStyle="black";
		ctx.fillRect(enemyCannonBalls[i][0],enemyCannonBalls[i][1],5,5);
		enemyCannonBalls[i][1]=enemyCannonBalls[i][1]+6;
		if(enemyCannonBalls[i][1]>=400){
			enemyCannonBalls.splice(i,1);
		}
	}
	if(enemyFire){//enemy will fire
		for(var i=0;i<invaders.length;i++){
			var ball=[invaders[i][0]+10,invaders[i][1]+20];
			enemyCannonBalls.push(ball);
		}
		enemyFire=false;
	}
	if(fire && cannonBalls.length<17){//you will fire
		var ball=[cannon[0],cannon[1]];
		cannonBalls.push(ball);
		fire=false;
	}else{
		fire==false;
	}
	if(dir=="left"){//move player left
		if(shooter[0]-10>=0){
			ctx.fillStyle="black";
			ctx.fillRect(shooter[0],shooter[1],40,10);
			ctx.fillRect(cannon[0],cannon[1],6,8);
			shooter[0]=shooter[0]-10;
			cannon[0]=cannon[0]-10;
			dir="";
		}
	}
	else if(dir=="right"){//move player right
		if(shooter[0]+40+10<=400){
			ctx.fillStyle="black";
			ctx.fillRect(shooter[0],shooter[1],40,10);
			ctx.fillRect(cannon[0],cannon[1],6,8);
			shooter[0]=shooter[0]+10;
			cannon[0]=cannon[0]+10;
			dir="";
		}
	}
	ctx.fillStyle="white";
	ctx.fillRect(shooter[0],shooter[1],40,10);//draw player
	ctx.fillRect(cannon[0],cannon[1],6,8);//draw cannon
	for(var i=0;i<cannonBalls.length;i++){//draw cannon balls
		ctx.fillStyle="white";
		ctx.fillRect(cannonBalls[i][0],cannonBalls[i][1],5,5);
	}
	for(var i=0;i<enemyCannonBalls.length;i++){//draw enemy cannon balls
		ctx.fillStyle="red";
		ctx.fillRect(enemyCannonBalls[i][0],enemyCannonBalls[i][1],5,5);
	}
}
function keyPush(event){//keypress
	map[event.keyCode] = true;
	if(map[32] && map[37]){
		fire=true;
		dir="left";
	}
	else if(map[32] && map[39]){
		fire=true;
		dir="right";
	}
	else if(map[32]){
		fire=true;
	}
	else if(map[37]){
		dir="left";
	}
	else if(map[39]){
		dir="right";
	}
}
function keyLift(event){
	map[event.keyCode]=false;
}
function invader(){//invader
	var x = Math.floor(Math.random()*360);
	inv=[x,0];
	invaders.push(inv);
	speed.push(Math.random()*4+1);
}