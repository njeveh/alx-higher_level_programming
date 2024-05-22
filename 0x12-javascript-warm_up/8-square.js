#!/usr/bin/node
const argv = require('process').argv;
const myNumber = argv[2];
if (isNaN(Number(myNumber))) {
  console.log('Missing size');
} else {
  let line = '';
  for (let j = myNumber; j > 0; --j) {
    line += 'X';
  }
  for (let i = 0; i < myNumber; ++i) {
    console.log(line);
  }
}
