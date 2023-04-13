/*
*   a function that returns the reversed version of a list:

*    Prototype: exports.esrever = function (list)
*    You are not allow to use the built-in method reverse
*/
#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  const last = list.length - 1;
  for (let i = last; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return (reversedList);
};