#!/usr/bin/node
const argv = require('process').argv
let myNumber = argv[2];
if (isNaN(Number(myNumber))) {
    console.log('Not a number');
} else {
    console.log(`My number: ${myNumber}`);
}
