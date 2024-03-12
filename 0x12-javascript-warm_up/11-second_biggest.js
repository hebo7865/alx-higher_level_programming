#!/usr/bin/node

const argList = process.argv.slice(2);
const num = argList.map(arg => Number(arg));

if (num.length < 2) {
  console.log(0);
} else {
  const sorted = num.sort((a, b) => b - a);
  console.log(sorted[1]);
}
