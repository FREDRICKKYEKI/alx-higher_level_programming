#!/usr/bin/node

//Write a script that prints x times “C is fun”

const times = new Number(process.argv[2]);
const str = 'C is fun';

// if is a number and exists
if (times && !isNaN(times)) {
  for (let i = 0; i < times; i++)
    console.log(str);
} else {
  console.log('Missing number of occurrences');
}
