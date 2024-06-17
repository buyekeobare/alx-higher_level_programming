#!/usr/bin/node

const process = require('process');
const argOne = process.argv[2];
const convertedArgOne = parseInt(argOne);

if (!isNaN(convertedArgOne)) {
  console.log('My number:', convertedArgOne);
} else {
  console.log('Not a number');
}
