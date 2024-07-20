#!/usr/bin/node
const args = process.argv[2];

const firstArg = Number(args);

if (Number.isInteger((firstArg))) {
  console.log(`My number: ${firstArg}`);
} else {
  console.log('Not a number');
}
