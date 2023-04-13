/*
*   a script that concats 2 files.

*    The first argument is the file path of the first source file
*    The second argument is the file path of the second source file
*    The third argument is the file path of the destination
*/
#!/usr/bin/node

const args = process.argv.slice(2);
const file = require('fs');
const contentA = file.readFileSync('./' + args[0]);
const contentB = file.readFileSync('./' + args[1]);
file.writeFileSync('./' + args[2], contentA + contentB);