#!/usr/bin/node
const argv = require('process').argv;
const occurrences = Number(argv[2]);

if (isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
    let num = occurrences;
  while (num > 0) {
    console.log('C is fun');
    --num;
  }
}
