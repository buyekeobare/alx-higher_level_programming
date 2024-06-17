#!/usr/bin/node

const process = require('process');
const argOne = process.argv[2];
const num = parseInt(argOne);

function calcFactorial (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x === 0) {
    return 1;
  } else {
    return x * calcFactorial(x - 1);
  }
}

if (!isNaN(num)) {
  console.log(calcFactorial(num));
} else {
  console.log('1');
}
