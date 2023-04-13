#!/usr/bin/node
/*
*   a script that prints the addition of 2 integers
*   The first argument is the first integer
*   The second argument is the second integer
*   You have to define a function with this prototype: function add(a, b)
*   You must use console.log(...) to print all output
*/
function add(a, b) {
x = parseInt(a);
y = parseInt(b);
result = x + y;
return result;
}

console.log(add(process.argv[2], process.argv[3]));
