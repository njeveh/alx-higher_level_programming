#!/usr/bin/node
const argv = require('process').argv;

function add (a, b) {
  return a + b;
}
const num1 = Number(argv[2]);
const num2 = Number(argv[3]);
const sum = add(num1, num2);
console.log(sum);
