#!/usr/bin/node
const Shape = require('./5-square');

class Square extends Shape {
  charPrint (c) {
    let row = '';
    for (let i = this.width; i > 0; i--) {
      if (c) {
        row += c;
      } else {
        row += 'X';
      }
    }
    for (let j = this.height; j > 0; j--) {
      console.log(row);
    }
  }
}

module.exports = Square;
