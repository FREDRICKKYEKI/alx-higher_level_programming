#!/usr/bin/node

/**
 * Write a script that concats 2 files.
 *
 * The first argument is the file path of the first source file
 * The second argument is the file path of the second source file
 * The third argument is the file path of the destination
 */

const fs = require('fs').promises;

async function concatFiles (files) {
  if (files.length !== 3) return;
  let filecontents = await fs.readFile(files[0], 'utf-8');
  filecontents += await fs.readFile(files[1], 'utf-8');

  await fs.writeFile(files[2], filecontents);
}

const files = process.argv.length > 2 ? process.argv.slice(2) : null;
concatFiles(files);
