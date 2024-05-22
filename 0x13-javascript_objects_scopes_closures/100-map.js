#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((key, x) => x * key);
console.log(list);
console.log(newList);
