#!/usr/bin/node
const argslen = process.argv.length;
if (argslen <= 2) {
  console.log('No argument');
} else if (argslen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
