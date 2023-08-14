#!/usr/bin/node

const times = Number(process.argv[2]);
const str = 'C is fun';

if (times && !isNaN(times)) {
  for (let i = 0; i < times; i++) { console.log(str); }
} else {
  console.log('Missing number of occurrences');
}
