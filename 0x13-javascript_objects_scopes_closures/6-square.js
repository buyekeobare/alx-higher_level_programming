#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let n = 0; n < this.width; n++) {
      let row = '';
      for (let m = 0; m < this.height; m++) {
        row += c;
      }
      console.log(row);
    }
  }
};
