#!/usr/bin/node
const argv = require('process').argv;
let occurenceNumber = argv[2];

if (isNaN(Number(occurenceNumber))) {
  console.log('Missing number of occurences');
} else {
  while (occurenceNumber > 0) {
    console.log('C is fun');
    --occurenceNumber;
  }
}
