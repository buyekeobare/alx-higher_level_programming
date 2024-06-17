#!/usr/bin/node

const process = require('process');
const oneArg = process.argv[2];

const x = parseInt(oneArg);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
