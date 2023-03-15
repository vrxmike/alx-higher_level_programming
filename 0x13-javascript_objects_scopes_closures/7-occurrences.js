#!/usr/bin/node
exports.nbOccurances = function (list, searchElement) {
  let nOccurances = 0;
  for (let i = 0; i < list.length; i++) {
   if (searchElement === list[i]) {
     nOccurrences++;
   }
  }
  return nOccurrences;
};
