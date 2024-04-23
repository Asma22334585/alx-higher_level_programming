#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + id, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  for (const x of JSON.parse(body).characters) {
    request.get(x, (error, response, bodyn) => {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(bodyn).name);
    });
  }
});
