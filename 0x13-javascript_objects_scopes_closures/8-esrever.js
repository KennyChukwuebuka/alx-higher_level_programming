#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};

/*
   exports.esrever = function (list) {
        return list.reduceRight(function (arr, cur) {
                arr.push(cur);
                return arr;
        }, []);
};
 */
