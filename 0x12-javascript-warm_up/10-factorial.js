#!/usr/bin/node
const argv = require('process').argv;
const num = Number(argv[2]);
if (isNaN(num)) {
  console.log(1);
} else {
  let factorial = 1;
  for (let i = num; i > 0; --i) {
    factorial *= i;
  }
  console.log(factorial);
}
