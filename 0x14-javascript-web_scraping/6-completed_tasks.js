#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const completed = {};
    for (const x of data) {
      if (x.completed === true) {
        if (x.userId in completed) {
          completed[x.userId]++;
        } else {
          completed[x.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
