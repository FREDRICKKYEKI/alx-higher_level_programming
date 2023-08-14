#!/usr/bin/node

/**
 * Write a function that increments and calls a function.

The function must be visible from outside
Prototype: function (number, theFunction)
You are not allowed to use var
 */

function addMeMaybe (number, theFunction) {
  let j = 0;

  for (let i = 0; i <= number; i++) j = i;
  j++;

  theFunction(j);
}

module.exports.addMeMaybe = addMeMaybe;
