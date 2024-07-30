#!/usr/bin/node
// A script that reads and prints the content of a file
const fs = require('fs');

// file path
const file = process.argv[2];

// Reads the contents of the file asynchronously
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    // If there was an error when reading the file, log the error object to the console
    console.error(err);
    return;
  }
  // If the file was successfully read, log its contents to the console
  console.log(data);
});
