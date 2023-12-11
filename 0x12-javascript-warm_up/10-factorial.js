#!/usr/bin/node

function calcFactorial (num) {
  if (isNaN(num)) {
    return 1;
  }
  if (num <= 1) {
    return 1;
  }
  return num * calcFactorial(num - 1);
}

const args = process.argv.slice(2);
const num = parseInt(args[0]);

const res = calcFactorial(num);
console.log(res);
