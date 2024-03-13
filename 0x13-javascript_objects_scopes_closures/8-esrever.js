#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - 1) > 0) {
    const exch = list[len];
    list[len] = list[i];
    list[i] = exch;
    i++;
    len--;
  }
  return list;
};
