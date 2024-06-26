#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

function doRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

request.get(url + id, async (error, response, body) => {
  if (error) {
    console.log(error);
  }
  for (const character of JSON.parse(body).characters) {
    console.log(JSON.parse(await doRequest(character)).name);
  }
}
);
