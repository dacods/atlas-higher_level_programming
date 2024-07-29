#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(body);

  const completedTask = {};

  todos.forEach(todo => {
    if (todo.completed) {
      completedTask[todo.userId] = 0;
    }
    completedTask[todo.userId]++;
  });
  console.log(completedTask);
});
