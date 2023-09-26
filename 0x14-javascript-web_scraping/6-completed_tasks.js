#!/usr/bin/node
/**
 * Write a script that computes the number of tasks completed by user id.
 * - The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * - Only print users with completed task
 * - You must use the module request
 */
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const complObj = {};
    for (const todo of JSON.parse(body)) {
      if (todo.completed) {
        if (complObj[todo.userId]) {
          complObj[todo.userId] = complObj[todo.userId] + 1;
        } else {
          complObj[todo.userId] = 1;
        }
      }
    }
    console.log(complObj);
  }
});
