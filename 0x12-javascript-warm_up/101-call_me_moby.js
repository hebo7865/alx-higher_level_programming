#!/usr/bin/node
const callMeMoby = function (x, theFunction) {
  if (x > 0) {
    theFunction();
    callMeMoby(x - 1, theFunction);
  }
};

module.exports.callMeMoby = callMeMoby;
