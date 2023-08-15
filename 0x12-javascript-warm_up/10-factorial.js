#!/usr/bin/node
const argv = require('process').argv;
function factorial (number) {
  if (isNaN(number) || number === 1) return 1;
  else {
    return number * factorial(number - 1);
  }
}

const num = argv[2];
console.log(factorial(num));
