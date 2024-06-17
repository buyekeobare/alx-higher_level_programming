#!/usr/bin/node

const process = require('process');
const oneArg = parseInt(process.argv[2]);
const twoArg = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(oneArg, twoArg));
