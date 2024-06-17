#!/usr/bin/node

const process = require('process');

const oneArg = process.argv;
const twoArg = process.argv;
console.log(oneArg[2] + ' is ' + twoArg[3]);
