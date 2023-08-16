#!/usr/bin/node

const Shape = require('./5-square.js');
class Square extends Shape {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let line = 'C';
      for (let i = 1; i < this.width; i++) {
        line = line + 'C';
      }
      for (let i = 0; i < this.height; i++) {
        console.log(line);
      }
    }
  }
}

module.exports = Square;
