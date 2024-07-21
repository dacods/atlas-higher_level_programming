#!/usr/bin/node
const args = process.argv;
const firstarg = Number(args[2]);
const secondarg = Number(args[3]);

function add (a, b) {
  console.log(a + b);
}

add(firstarg, secondarg);
