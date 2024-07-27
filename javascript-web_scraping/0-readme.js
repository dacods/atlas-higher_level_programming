#!/usr/bin/node
const fs = require('fs');

const filepath = process.argv[2];

fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
