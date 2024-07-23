#!/usr/bin/node
exports.esrever = function (list) {
  const reList = [];
  while (list.length) {
    reList.push(list.pop());
  }

  return reList;
};
