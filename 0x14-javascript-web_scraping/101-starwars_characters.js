#!/usr/bin/node
/**
 * Write a script that prints all characters of a Star Wars movie:
 * - The first argument is the Movie ID
 *        - example: 3 = “Return of the Jedi”
 * - Display one character name by line in the same order of the list
 *  “characters” in the /films/ response
 * - You must use the Star wars API
 * - You must use the module request
 */
const request = require('request');

let id = parseInt(process.argv[2]);
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;

    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }

    results.forEach((result) => {
      if (result.episode_id == id) {
        result.characters.forEach((char) => {
          request(char, (err2, res2, body2) => {
            if (err2) return;
            else {
              console.log(JSON.parse(body2).name);
            }
          });
        });
      }
    });
  }
});
