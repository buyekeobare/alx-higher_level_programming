#!/usr/bin/node
// A script that writes data to a file
const fs = require('fs');

// file path
const file = process.argv[2];

// writes to file
fs.writeFile(file, process.argv[3], { flag: 'w' }, (err) => {
  if (err) {
    console.log(err);
  }
});
