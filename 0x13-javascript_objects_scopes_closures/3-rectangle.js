#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let x = ' ';
      for (let j = 0; j < this.width; j++) {
        x += 'x';
      }
      console.log(x);
    }
  }
};
module.exports = Rectangle;
  