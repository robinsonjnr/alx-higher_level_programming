#!/usr/bin/node
/*
*   a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

*    Your script must import dict from the file 101-data.js
*    In the new dictionary:
        A key is a number of occurrences
        A value is the list of user ids
*    Print the new dictionary at the end
*/

const originalList = require('./100-data').list;
console.log(originalList);
const mappedList = originalList.map (function (e, index) {
  return (e * index);
});
console.log(mappedList);