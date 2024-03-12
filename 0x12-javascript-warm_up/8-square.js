#!/usr/bin/node

const arg = process.argv[2];
const square = Number(arg)

if (isNaN(square)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < square; i++) {
    console.log('x'.repeat(square));
  }
}
