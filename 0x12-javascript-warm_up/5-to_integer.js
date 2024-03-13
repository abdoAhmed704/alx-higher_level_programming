#!/usr/bin/node
let argstr = process.argv[2];
let convertedNum = parseInt(argstr);
if (convertedNum == "NaN" || process.argv.length == 2){
	console.log("Not a number");
} else{
	console.log("My number: "+ convertedNum);
}
