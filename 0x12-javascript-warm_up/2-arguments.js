#!/usr/bin/node

const count_args = process.argv.length - 2;

if (count_args === 0) {
  console.log('No argument');
} else if (count_args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
