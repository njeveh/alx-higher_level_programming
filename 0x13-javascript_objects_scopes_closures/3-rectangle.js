#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = this.height; i > 0; i--) {
      let line = '';
      for (let j = this.width; j > 0; j--) {
        line = 'X';
      }
      console.log(line);
    }
  }
}

module.exports = Rectangle;
