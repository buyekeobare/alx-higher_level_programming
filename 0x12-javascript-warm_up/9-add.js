#!/usr/bin/node

const process = require('process');
const arg_one = parseInt(process.argv[2]);
const arg_one = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(arg_one, arg_two));
