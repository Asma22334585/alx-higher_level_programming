#!/usr/bin/node

const Dict = require('./101-data').dict;
const newDict = {};

for (const key in Dict) {
  if (newDict[Dict[key]] === undefined) {
    newDict[Dict[key]] = [];
  }
  newDict[Dict[key]].push(key);
}
console.log(newDict);
