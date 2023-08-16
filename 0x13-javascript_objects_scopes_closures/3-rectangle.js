#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let w = '';
    for (let i = this.width; i > 0; --i) {
      w += 'X';
    }
    for (let j = this.height; j > 0; --j) {
      console.log(w);
    }
  }
}
