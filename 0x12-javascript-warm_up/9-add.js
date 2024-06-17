#!/usr/bin/node

const process = require('process');
const argOne = parseInt(process.argv[2]);
const argTwo = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(argOne, argTwo));
