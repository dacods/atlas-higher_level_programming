#!/usr/bin/node
const args = process.argv.slice(2);

const [arg1 = 'undefined', arg2 = 'undefined'] = args;

console.log(`${arg1} is ${arg2}`);
