#!/usr/bin/node
/**
 * Write a script that writes a string to a file.
 * - The first argument is the file path
 * - The second argument is the string to write
 * - The content of the file must be written in utf-8
 * - If an error occurred during while writing, print the error object
 */
const fs = require('fs');

const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(filename, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
