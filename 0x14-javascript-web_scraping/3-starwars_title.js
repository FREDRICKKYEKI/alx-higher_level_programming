#!/usr/bin/node
/**
 * Write a script that prints the title of a Star Wars movie where the
 * episode number matches a given integer.
 * - The first argument is the movie ID
 * - You must use the Star wars API with the endpoint
 *   https://swapi-api.alx-tools.com/api/films/:id
 * - You must use the module request
 */
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
