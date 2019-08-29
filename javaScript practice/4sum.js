// Shahroz Imtiaz
// 1/9/2018
window.onload=function(){
	canv=document.getElementById("gc");
	ctx=canv.getContext("2d");
	timer = setInterval(loop,1000); // calling loop function
}
readNumbers = [] //array of the inputted numbers
i = 0 //used for indexing the array
counter = 0; //used to keep track of how many numbers have been read in
function loop() {
	counter++
	readNumbers[i] = parseInt(prompt()) //used to grab next int input
	console.log(readNumbers + "..." + counter) //used for ensuring the correctness of my code
	if(i!=0 && counter==4 && i<=100){ //every 4 numbers, you have to output the sum of it and the last 3 nums
		sum = readNumbers[i] + readNumbers[i-1] + readNumbers[i-2] + readNumbers[i-3]
		console.log(sum)
		counter=0; //reset counter for the next set of 4 numbers
	}
	i++ //indexing
}