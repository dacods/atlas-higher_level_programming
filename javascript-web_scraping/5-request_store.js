#!/usr/bin/node
const request = require('request');

const fs = require('fs');

const url = process.argv[2];

const filepath = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(filepath, body, 'utf8', () => {});
});
