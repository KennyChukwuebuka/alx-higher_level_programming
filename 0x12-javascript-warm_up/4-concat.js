#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length >= 1) {
    const firstArg = args[0];
    const secondArg = args.length > 1 ? args[1] : "undefined";
    console.log(`${firstArg} is ${secondArg}`);
} else {
    console.log(`undefined is undefined`);
}
