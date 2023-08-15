#!/usr/bin/node

/**
 * Write a class Square that defines a square and inherits from Square of 5-square.js:
 *
 * You must use the class notation for defining your class and extends
 * Create an instance method called charPrint(c) that prints the rectangle using the character c
 * If c is undefined, use the character X
 */

const Rectangle = require('./4-rectangle');

class Square extends  Rectangle{
  constructor (size) {
    super(size, size)
  }

  charPrint(c = 'X') {
    let w = this.width;
    let h = this.height;
    let row;

    for (let i = 0; i < h; i++) {
      row = '';
      for (let j = 0; j < w; j ++) {
        row += c;
      }
      console.log(row);
    }

  }

}

module.exports = Square;
