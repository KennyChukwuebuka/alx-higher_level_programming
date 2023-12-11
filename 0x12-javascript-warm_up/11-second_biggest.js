#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const integer = args.map(Number);
  integer.sort((a, b) => b - a);

  const sLarge = integer[1];
  console.log(sLarge);
}
