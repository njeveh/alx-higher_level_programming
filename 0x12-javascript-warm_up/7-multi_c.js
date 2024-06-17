#!/usr/bin/node
const arguments = require('process').argv;
let occurrences = Number(arguments[2]);
if (isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  while (occurrences > 0) {
    console.log('C is fun');
    --occurrences;
  }
}
