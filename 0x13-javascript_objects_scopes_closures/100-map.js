#!/usr/bin/node
const list = require('./list-100.js').list;
let newList = [];
newList = list.map((item, index) => item * index);
console.log(list);
console.log(newList);