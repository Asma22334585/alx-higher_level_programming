#!/usr/bin/node
const initialList = require('./100-data.js').list;
const newList = initialList.map((number, index) => number * index);

console.log(initialList);
console.log(newList);
