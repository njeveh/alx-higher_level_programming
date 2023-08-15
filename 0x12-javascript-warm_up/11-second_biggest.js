#!/usr/bin/node
const argv = require('process').argv;
const argumentsCount = argv.length;
if (argumentsCount === 2 || argumentsCount === 3) {
  console.log(0);
} else {
  const arr = [Number(argv[2]), Number(argv[2])];
  for (let i = 3; i < argumentsCount; ++i) {
    if (Number(argv[i]) > arr[0]) {
      arr[1] = arr[0];
      arr[0] = Number(argv[i]);
    }
  }
  console.log(arr[1]);
}
