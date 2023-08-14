#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial(n) {
  if (n == 0) {
    return (1);
  }
  return n * factorial(n - 1);
}

if (Number.isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num))
}
