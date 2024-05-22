#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (let i = list.length - 1; i >= 0; --i) {
    if (list[i] === searchElement) {
      ++occurences;
    }
  }
  return occurences;
};
