#!/usr/bin/node
const argv = require('process').argv;
const size = Number(argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let height = 0; height < size; height++) {
    let line = '';
    for (let width = 0; width < size; width++) {
      line += 'X';
    }
    console.log(line);
  }
}
