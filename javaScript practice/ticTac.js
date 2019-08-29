window.onload = function () {
    canv = document.getElementById('gc');
    ctx = canv.getContext('2d');
    document.addEventListener("mousedown", click);
    boardpic = new Image();
    requestAnimationFrame(game);
};
board = [];
board.push([]);
board.push([]);
board.push([]);
let i=-1;
let j=-1;
player1 = true;
cords = [];
markers = new Map();
function game() {
    boardpic.src="tac.jpg";
    boardpic.onload = () => {
        ctx.fillStyle="white";
        ctx.fillRect(0,0,canv.width,canv.height);
        ctx.drawImage(boardpic, 0, 0, 500, 500);
    };
    ctx.fillStyle = "black";
    ctx.font = "14px Georgia";
    if(player1){
        ctx.fillText("Turn: black",0,550);
    }else{
        ctx.fillText("Turn: orange",0,550);
    }
    markers.forEach(draw);
    if(markers.size==9){
        alert("draw");
        reset();
    }
    requestId = requestAnimationFrame(game);
}
function draw(value, key, map) {
    if (key.mark == true) {
        ctx.fillStyle = "black";
        ctx.fillRect(key.x + 30, key.y + 30, 40, 40);
    } else {
        ctx.fillStyle = "orange";
        ctx.fillRect(key.x + 30, key.y + 30, 40, 40);
    }
}
function click(mouse) {
console.log(mouse.x + ' ' + mouse.y);

    if(mouse.x>38 && mouse.x<187){
        i=0;
        cords[0]=38;
    }
    if(mouse.x>=187 && mouse.x<338){
        i=1;
        cords[0]=187;
    }
    if(mouse.x>=338 && mouse.x<482){
        i=2;
        cords[0]=338;
    }

    if(mouse.y>28 && mouse.y<187){
        j=0;
        cords[1]=28;
    }
    if(mouse.y>=187 && mouse.y<338){
        j=1;
        cords[1]=187;
    }
    if(mouse.y>=338 && mouse.y<482){
        j=2;
        cords[1]=338;
    }
    mark = new Marker(player1,cords[0],cords[1]);
    if(i!=-1 && j!=-1){
        if(board[i][j]==undefined){
            markers.set(mark,1);
            board[i][j] = mark;
            player1=!player1;
            logicCheck(mark,i,j);
        }
        i=j=-1;
    }
}
function logicCheck(mark,i,j) {
    var count = 0;
    //horizontal
    for(var x=0;x<=2;x++){
        if(board[x][j]==undefined){
            break;
        }
        else if(board[x][j].mark==mark.mark){
            count++;
        }else{
            break;
        }
    }
    winnerCheck(mark.mark,count,true);
    count=0;
    //vertical
    for(var y=0;y<=2;y++){
        if(board[i][y]==undefined){
            break;
        }
        else if(board[i][y].mark==mark.mark){
            count++;
        }else{
            break;
        }
    }
    winnerCheck(mark.mark,count,true);
    count=0;
    //diagonal
    var seen = false;
    for(var x=0;x<=2;x++) {
        if(board[x][x]==undefined){
            break;
        }
        else if(board[x][x].mark==mark.mark){
            if(i==x && j==x){
                seen = true;
            }
            count++;
        }else{
            break;
        }
    }
    winnerCheck(mark.mark,count,seen);
    count=0;
    for(var x=0,y=2;x<=2;x++,y--) {
        if(board[x][y]==undefined){
            break;
        }
        else if(board[x][y].mark==mark.mark){
            if(i==x && j==y){
                seen = true;
            }
            count++;
        }else{
            break;
        }
    }
    winnerCheck(mark.mark,count,seen);
}
function winnerCheck(turn,count,seen) {
    var person = "";
    if(turn == true){
        person = "black";
    }else{
        person = "orange";
    }
    if(count==3 && seen){
        alert("Winner: " + person);
       reset();
    }
}
function reset() {
    board = [];
    board.push([]);
    board.push([]);
    board.push([]);
    i=-1;
    j=-1;
    player1 = true;
    cords = [];
    markers = new Map();
}
class Marker{
    constructor(marker,x, y) {
        this.mark = marker;
        this.x = x;
        this.y = y;
    }
    // addMarker(player){
    //     this.mark=player;
    // }
}