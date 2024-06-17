#!/usr/bin/node
const arguments = require('process').argv;
if (isNaN(Number(arguments[2]))) {
    console.log('Not a number');
} else {
    console.log(`My number: ${arguments[2]}`)
}