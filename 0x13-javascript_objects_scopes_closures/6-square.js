#!/usr/bin/node
const SquareAS = require('./5-square');

class Square extends SquareAS {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += c;
      }
      console.log(x);
    }
  }
}

module.exports = Square;
