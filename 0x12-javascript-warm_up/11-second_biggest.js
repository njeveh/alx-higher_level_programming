#!/usr/bin/node
const argv = require('process').argv;
const argumentsCount = argv.length;
const numbers = [];
if (argumentsCount <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argumentsCount; i++) {
    numbers.push(Number(argv[i]));
  }
  numbers.sort();
  numbers.reverse();
  console.log(numbers[1]);
}
