#!/usr/bin/node

/**
 * Write a function that returns the reversed version of a list:
 *
 * Prototype: exports.esrever = function (list)
 * You are not allow to use the built-in method reverse
 */

module.exports.esrever = function (list) {
  let reversedList = [];
  let i = list.length - 1;

  while (i >= 0) {
    reversedList.push(list[i]);
    i--;
  }

  return (reversedList);
}
