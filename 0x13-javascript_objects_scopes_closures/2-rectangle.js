#!/usr/bin/node

class Rectangle {
  width;
  height;
  constructor (w, h) {
    if (h === 0 || w === 0) {
      return {};
    }
    this.height = h;
    this.width = w;
  }
}

module.exports = Rectangle;
