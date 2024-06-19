#!/usr/bin/node

exports.esrever = function (list) {
  listLength = list.length;
  reversedList = [];
  for (let i = listLength - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
