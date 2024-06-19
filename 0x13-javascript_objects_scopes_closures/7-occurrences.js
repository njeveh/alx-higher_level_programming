#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const filteredList = list.filter(element => element === searchElement);
  return filteredList.length;
};
