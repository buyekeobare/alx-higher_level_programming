#!/usr/bin/node

const process = require('process');
const arg_one = process.argv[2];
const num = parseInt(arg_one);

function factorial (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

if (!isNaN(num)) {
  console.log(factorial(num));
} else {
  console.log('1');
}
