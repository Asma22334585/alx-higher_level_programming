#!/usr/bin/node

exports.converter = function (base) {
  return function (nmbr) {
    return nmbr.toString(base);
  };
};
