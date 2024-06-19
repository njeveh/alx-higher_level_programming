#!/usr/bin/node
const list = require('./list-100').list;

const newList = list.map((item, index) => item * index);
console.log(list);
console.log(newList);
