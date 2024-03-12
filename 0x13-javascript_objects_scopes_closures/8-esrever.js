#!/usr/bin/node
exports.esrever = function (list) {
  const eversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    eversedList.push(list[i]);
  }
  return eversedList;
};
