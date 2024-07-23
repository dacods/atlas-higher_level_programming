#!/usr/bin/node
exports.esrever = function (list) {
  const re_list = [];
  while (list.length) {
    re_list.push(list.pop());
  }

  return re_list;
};
