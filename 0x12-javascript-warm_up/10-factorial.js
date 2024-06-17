#!/usr/bin/node
const argv = require('process').argv;
const num = Number(argv[2]);

function factorial (num) {
  if (num === 1 || num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
