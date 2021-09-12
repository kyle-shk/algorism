// let a = [10, 11, 9, 3, 6, 5, 4];
// let 정렬된배열 = [];

// for (var i = 0; i < 7; i++) {
//   정렬된배열.push(Math.min.apply(null, a));
//   a.splice(a.indexOf(Math.min.apply(null, a)), 1);
//   console.log(a);
//   console.log("----");
//   console.log(정렬된배열);
// }

// var selectionSort = function(array) {
//   var length = array.length;
//   var minIndex, temp, i, j;
//   for (i = 0; i < length - 1; i++) { // 처음부터 훑으면서
//     minIndex = i;
//     for (j = i + 1; j < length; j++) { // 최솟값의 위치를 찾음
//       if (array[j] < array[minIndex]) {
//         minIndex = j;
//       }
//     }
//     temp = array[minIndex]; // 최솟값을 저장
//     array[minIndex] = array[i];
//     array[i] = temp; // 최솟값을 제일 앞으로 보냄
//   }
//   return array;
// };

// selectionSort([5,1,4,7,2,6,8,3]); // [1,2,3,4,5,6,7,8]
const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString();
console.log(input);
input = input.split("\n");
console.log(input);
