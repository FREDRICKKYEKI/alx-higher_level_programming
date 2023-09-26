#!/usr/bin/node
/**
 * Write a script that prints all characters of a Star Wars movie:
 * - The first argument is the Movie ID
 *      example: 3 = “Return of the Jedi”
 * - Display one character name by line
 * - You must use the Star wars API
 * - You must use the module request
 */
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body);
    results.characters.forEach((char) => {
      request(char, (err2, res2, body2) => {
        if (err2) return;
        else {
          console.log(JSON.parse(body2).name);
        }
      });
    });
  }
});
