#!/usr/bin/node
const fh = require('fs');
const args = require('process').argv;

let fileOneContent = '';
let fileTwoContent = '';
fh.readFile(args[2], 'utf8', (err, data) => {
  if (err) throw err;
  fileOneContent = data;
});
fh.readFile(args[3], 'utf8', (err, data) => {
  if (err) throw err;
  fileTwoContent = data;
});
fh.writeFile(args[4], fileOneContent, (err) => {
  if (err) throw err;
});
fh.appendFile(args[4], fileTwoContent, function (err) {
  if (err) throw err;
});
