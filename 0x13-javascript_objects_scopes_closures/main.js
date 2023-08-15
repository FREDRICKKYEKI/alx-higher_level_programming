#!/usr/bin/node
// const Rectangle = require('./0-rectangle');

// const r1 = new Rectangle();
// console.log(r1);
// console.log(r1.constructor);

// const Rectangle = require('./1-rectangle');

// const r1 = new Rectangle(2, 3);
// console.log(r1);
// console.log(r1.width);
// console.log(r1.height);

// const r2 = new Rectangle(2, -3);
// console.log(r2);
// console.log(r2.width);
// console.log(r2.height);

// const r3 = new Rectangle(2);
// console.log(r3);
// console.log(r3.width);
// console.log(r3.height);

// const Rectangle = require('./2-rectangle');

// const r1 = new Rectangle(2, 3);
// console.log(r1);
// console.log(r1.width);
// console.log(r1.height);

// const r2 = new Rectangle(2, -3);
// console.log(r2);
// console.log(r2.width);
// console.log(r2.height);

// const r3 = new Rectangle(2);
// console.log(r3);
// console.log(r3.width);
// console.log(r3.height);

// const r4 = new Rectangle(2, 0);
// console.log(r4);
// console.log(r4.width);
// console.log(r4.height);

// const Rectangle = require('./3-rectangle');

// const r1 = new Rectangle(2, 3);
// r1.print();

// const r2 = new Rectangle(10, 5);
// r2.print();

// const Rectangle = require('./4-rectangle');

// const r1 = new Rectangle(2, 3);
// console.log('Normal:');
// r1.print();

// console.log('Double:');
// r1.double();
// r1.print();

// console.log('Rotate:');
// r1.rotate();
// r1.print();

// const Square = require('./5-square');

// const s1 = new Square(4);
// s1.print();
// s1.double();
// s1.print();

// const Square = require('./6-square');

// const s1 = new Square(4);
// s1.charPrint();

// s1.charPrint('C');

// const nbOccurences = require('./7-occurrences').nbOccurences;

// console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
// console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
// console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));

// const esrever = require('./8-esrever').esrever;

// console.log(esrever([1, 2, 3, 4, 5]));
// console.log(esrever(["School", 89, { id: 12 }, "String"]));

// const logMe = require('./9-logme').logMe;

// logMe("Hello");
// logMe("Best");
// logMe("School");

const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));
