#!/usr/bin/node

const arg1 = Number(process.argv[2]);

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(arg1));
