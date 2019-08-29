window.onload=function(){
    canv = document.getElementById("gc");
    ctx = canv.getContext("2d");
    document.addEventListener("mousedown", click);
    document.addEventListener("mousemove", move);
    document.addEventListener("mouseup", letGo);
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canv.width, canv.height);
    requestAnimationFrame(draw);
}
lines = []
line = []
clicked = false;
function draw(){
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canv.width, canv.height);
    for(var i = 0;i<lines.length;i++){
        var line = lines[i];
        drawLine(line[0], line[1], line[2], line[3]);
    }
    if(line != null && clicked){
        drawLine(line[0], line[1], line[2], line[3]);
        console.log(line[3])
    }
}
function drawLine(fromx, fromy, tox, toy) {
    console.log("filled");
    ctx.strokeStyle = "white";
    ctx.beginPath();
    ctx.moveTo(fromx, fromy);
    ctx.lineTo(tox, toy);
    ctx.stroke();
}
function click(mouse) {
  clicked = true;
  line[0]=mouse.x;
  line[1]=mouse.y;
}
function move(mouse){
    if(clicked){
        line[2]=mouse.x;
        line[3]=mouse.y;
        // draw();
        ctx.fillStyle="white";
        ctx.fillRect(mouse.x,mouse.y,5,5)
        // drawLine(line[0], line[1], line[2], line[3]);
    }
}
function letGo(mouse) {
    clicked=false;
    lines.push(line);
    line=[]
}