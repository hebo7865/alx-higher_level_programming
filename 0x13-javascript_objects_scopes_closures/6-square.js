#!/usr/bin/node

const Squa = require('./5-square');

class Square extends Squa {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let squ = '';
      for (let j = 0; j < this.width; j++) {
        squ += c;
      }
      console.log(squ);
    }
  }
}
module.exports = Square;
