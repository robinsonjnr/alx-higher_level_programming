#!/usr/bin/node
/*
*  a script that prints the first argument passed to it:
*   If no arguments are passed to the script, print “No argument”
*   You must use console.log(...) to print all output
*/
const first_arg = process.argv[2];
if (first_arg === undefined) {
  console.log('No argument');
} else {
  console.log(first_arg);
}
