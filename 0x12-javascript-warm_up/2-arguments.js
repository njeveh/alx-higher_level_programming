#!/usr/bin/node

const {argv} = require('node:process');
const numberOfArguments = argv.length;
if (numberOfArguments === 2) {
    console.log('No argument');
}
else if (numberOfArguments === 3) {
    console.log('Argument found');
}
else if (numberOfArguments > 3) {
    console.log('Arguments found');
}
