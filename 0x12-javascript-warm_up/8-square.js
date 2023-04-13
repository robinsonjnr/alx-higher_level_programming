#!/usr/bin/node
/*
*   a script that prints a square
*   The first argument is the size of the square
*   If the first argument can’t be converted to an integer, print “Missing size”
*   you must use the character X to print the square
*   You must use console.log(...) to print all output
*   You are not allowed to use var
*/
const arg = parseInt(process.argv[2]);

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i <= arg; i++) {
            console.log('x'.repeat(arg));
    }
  }
}
