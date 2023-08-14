#!/usr/bin/node

const size = parseInt(process.argv[2]);

function printSquare(size) {
  let w;
  for (let i = 0; i < size; i++) {
    w = '';
    for (let j = 0; j < size; j++) {
      w += 'x';
    }
    console.log(w);
  }

}

if (!Number.isNaN(size)) printSquare(size);
else console.log("Missing size");
