#!/usr/bin/node
const request = require('request');

const args = process.argv[2];

const url = args || 'https://swapi-api.hbtn.io/api/films/';

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach(film => {
    film.characters.forEach(url => {
      if (url.includes('/18/')) {
        count++;
      }
    });
  });
  console.log(count);
});
