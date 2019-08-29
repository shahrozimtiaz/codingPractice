//Shahroz Imtiaz
//1/10/2019
window.onload=function() {
	canv=document.getElementById("gc");
	ctx=canv.getContext("2d");
	document.addEventListener("keydown",keyPush);
	image = new Image("apple.jpg");
	image.src="apple.jpg";
	timer = setInterval(game,100);
}
food = [Math.floor(Math.random()*20)*20, Math.floor(Math.random()*20)*20];
snake = [[140,140],[120,140],[100,140],[80,140]];
prevKey = 39;
dir="right";
score = 0;
function game(){
	for(var i=0;i<snake.length;i++){
		if(snake[0][0]==snake[i][0] && snake[0][1]==snake[i][1] && i!=0){	
			clearInterval(timer);
			alert("Game Over");
			break;
		}
	}
	ctx.fillStyle="black";
	ctx.fillRect(0,0,canv.width,canv.height);
	ctx.fillStyle="white";
	ctx.font = "14px Georgia";
	ctx.fillText("Score: " + score,0,11);
	ctx.fillStyle="white";
	ctx.font = "14px Georgia";
	ctx.fillText("Shahroz Imtiaz ",285,392);
	ctx.fillStyle="red";
	ctx.drawImage(image, food[0],food[1],20,20);
	if(snake[0][0]>380 || snake[0][0]<0 || snake[0][1]>380 || snake[0][1]<0 ){
		clearInterval(timer);
		alert("Game Over");
	}
	if(snake[0])
	if(snake[0][0]==food[0] && snake[0][1]==food[1]){
		ctx.fillStyle="black";
		ctx.fillRect(food[0],food[1], 20, 20);
		snake.unshift(food);
		score++;
		food = [Math.floor(Math.random()*20)*20, Math.floor(Math.random()*20)*20];
	}

	if(dir=="left"){ //left->up->right->down
		var earse = snake.pop();
		ctx.fillStyle="black";
		ctx.fillRect(earse[0],earse[1], 20, 20);
		snake.unshift([snake[0][0]-20, snake[0][1]]);
		prevKey=37;
		dir="left";
	}
	else if(dir=="up"){
		var earse = snake.pop();
		ctx.fillStyle="black";
		ctx.fillRect(earse[0],earse[1], 20, 20);
		snake.unshift([snake[0][0], snake[0][1]-20]);
		prevKey=38;
		dir="up";
	}
	else if(dir=="right"){
		var earse = snake.pop();
		ctx.fillStyle="black";
		ctx.fillRect(earse[0],earse[1], 20, 20);
		snake.unshift([snake[0][0]+20, snake[0][1]]);
		prevKey=39;
		dir="right";
	}
	else if(dir=="down"){
		var earse = snake.pop();
		ctx.fillStyle="black";
		ctx.fillRect(earse[0],earse[1], 20, 20);
		snake.unshift([snake[0][0], snake[0][1]+20]);
		prevKey=40;
		dir="down";
	}
	ctx.fillStyle="lime";
	for(var i=0;i<snake.length;i++){
		ctx.fillRect(snake[i][0],snake[i][1],20,20);
	}
	eyesTongue(dir);
}
function keyPush(event){
	if(event.keyCode==37){ //left->up->right->down
		dir="left";
	}
	else if(event.keyCode==38){
		dir="up";
	}
	else if(event.keyCode==39){
		dir="right";
	}
	else if(event.keyCode==40){
		dir="down";
	}
}
function eyesTongue(dir){
	if(dir=="left"){
		ctx.fillStyle="yellow";
		ctx.fillRect(snake[0][0]+6,snake[0][1]+2, 5, 5);
		ctx.fillRect(snake[0][0]+6,snake[0][1]+13.2, 5, 5);
		ctx.fillStyle="red";
		ctx.fillRect(snake[0][0]-10,snake[0][1]+10, 10, 5);
	}
	else if(dir=="up"){
		ctx.fillStyle="yellow";
		ctx.fillRect(snake[0][0]+2,snake[0][1]+6, 5, 5);
		ctx.fillRect(snake[0][0]+13.2,snake[0][1]+6, 5, 5);
		ctx.fillStyle="red";
		ctx.fillRect(snake[0][0]+10,snake[0][1]-10, 5, 10);
	}
	else if(dir=="right"){
		ctx.fillStyle="yellow";
		ctx.fillRect(snake[0][0]+14,snake[0][1]+2, 5, 5);
		ctx.fillRect(snake[0][0]+14,snake[0][1]+13.2, 5, 5);
		ctx.fillStyle="red";
		ctx.fillRect(snake[0][0]+20,snake[0][1]+10, 10, 5);
	}
	else if(dir=="down"){
		ctx.fillStyle="yellow";
		ctx.fillRect(snake[0][0]+2,snake[0][1]+14, 5, 5);
		ctx.fillRect(snake[0][0]+13.2,snake[0][1]+14, 5, 5);
		ctx.fillStyle="red";
		ctx.fillRect(snake[0][0]+10,snake[0][1]+20, 5, 10);
	}
}