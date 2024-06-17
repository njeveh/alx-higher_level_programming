#!/usr/bin/node
const arguments = require('process').argv;
if (isNaN(Number(arguments[2]))) {
  console.log('Missing number of occurrences');
} else {
  let occurrences = Number(arguments[2]);
  while (occurrences) {
    console.log('C is fun');
    --occurrences;
  }
}
