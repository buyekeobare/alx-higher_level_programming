#!/usr/bin/node

const process = require('process');

const value_args = process.argv;
if (value_args[2]) {
  console.log(value_args[2]);
} else {
  console.log('No argument');
}
