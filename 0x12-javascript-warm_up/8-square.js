#!/usr/bin/node

const arg = process.argv[2];
const square = parseInt(arg);

if (isNaN(square) || square == undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < square; i++) {
    console.log('x'.repeat(square));
  }
}
