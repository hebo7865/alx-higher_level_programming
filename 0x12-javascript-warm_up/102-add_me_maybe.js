#!/usr/bin/node
const addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};

module.exports.addMeMaybe = addMeMaybe;
