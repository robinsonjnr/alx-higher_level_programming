/*
*   a function that returns the number of occurrences in a list:

*    Prototype: exports.nbOccurences = function (list, searchElement)
*/
#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(e => e === searchElement).length);
};