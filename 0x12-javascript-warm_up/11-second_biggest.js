#!/usr/bin/node

const args = process.argv;

function findSecondMax (arr) {
  const sorted = [...arr].sort((a, b) => b - a);

  return (sorted[1]);
}

if (args.length <= 3) {
  console.log(0);
} else {
  const nums = args.slice(2);
  const intArr = [...nums.map(n => parseInt(n))];

  console.log(findSecondMax(intArr));
}
