#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      let row = '';
      for (let m = 0; m < this.width; m++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
