#!/usr/bin/node

function add(a, b) {
	return a + b;;
}

const args = process.argv.slice(2);
const firstArgs = parseInt(args[0]);
const secondArgs = parseInt(args[1]);

if (!isNaN(firstArgs) && !isNaN(secondArgs)) {
	const res = add (firstArgs, secondArgs);
	console.log(res);
} else {
	console.log("NaN");
}
