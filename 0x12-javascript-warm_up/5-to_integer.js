#!/usr/bin/node

const args = process.argv.slice(2);

const argsAsInt = parseInt(args[0]);

if (!isNaN(argsAsInt)) {
  console.log(`My number: ${argsAsInt}`);
} else {
  console.log('Not a number');
}
