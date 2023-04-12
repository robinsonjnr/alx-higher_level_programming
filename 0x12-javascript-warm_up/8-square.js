#!/usr/bin/node
/*
*   a script that prints a square
*   The first argument is the size of the square
*   If the first argument can’t be converted to an integer, print “Missing size”
*   you must use the character X to print the square
*   You must use console.log(...) to print all output
*   You are not allowed to use var
*/
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i <= parseInt(process.argv[2]); i++) {
            console.log(x.repeat(parseInt(process.argv[2])));
    }
  }
}