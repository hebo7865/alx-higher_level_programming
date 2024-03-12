#!/usr/bin/node

const arg = process.argv[2];
const square = Number(arg);

if (isNaN(square) || square === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < square; i++) {
    console.log('X'.repeat(square));
  }
}
