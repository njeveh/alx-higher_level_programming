#!/usr/bin/node
const argv = require('process').argv;
const num1 = Number(argv[2]);
const num2 = Number(argv[3]);

function add (a, b) {
  return a + b;
}
console.log(add(num1, num2));
