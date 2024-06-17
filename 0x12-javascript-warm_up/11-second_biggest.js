#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (isNaN(args[2]) || isNaN(args[3])) {
  console.log('0');
} else {
  const myArray = args.map(Number);
  myArray.slice(2, args.length);
  myArray.sort((a, b) => a - b);
  console.log(myArray[myArray.length - 2]);
}
