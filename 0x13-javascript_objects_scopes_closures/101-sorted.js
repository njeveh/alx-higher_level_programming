#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const k in dict) {
  if (!(dict[k] in newDict)) {
    newDict[dict[k]] = [k];
  } else {
    newDict[dict[k]].push(k);
  }
}
