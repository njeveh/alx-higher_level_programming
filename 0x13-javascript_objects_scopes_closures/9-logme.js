#!/usr/bin/node

exports.logMe = function (item) {
  class LogCount {
    static count = 0;
  }
  console.log(`${LogCount.count}: ${item}`);
  ++LogCount.count;
};
