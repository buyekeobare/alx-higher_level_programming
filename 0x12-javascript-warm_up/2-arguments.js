#!/usr/bin/node

const countArgs = process.argv.length - 2;

if (countArgs === 0) {
  console.log('No argument');
} else if (countArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
