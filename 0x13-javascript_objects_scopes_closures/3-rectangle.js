#!/usr/bin/node

/**
 * Write a class Rectangle that defines a rectangle:
 *
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments: w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * Create an instance method called print() that prints the rectangle using the character X
 */

class Rectangle {
  constructor (w, h) {
    if (w && w !== 0 && w > 0 && h && h !== 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    let w = this.width;
    let h = this.height;
    let row;

    for (let i = 0; i < h; i++) {
      row = '';
      for (let j = 0; j < w; j ++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
