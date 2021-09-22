function solution(a, b, c) {
  for (let i = 0; i < a; i++) {
    if (b[i] === c[i]) {
      console.log("D");
    } else if (b[i] < c[i]) {
      console.log("B");
    } else if (b[i] === 3 && c[i] === 1) {
      console.log("B");
    } else {
      console.log("A");
    }
  }
}

let arr1 = [2, 3, 3, 1, 3];
let arr2 = [1, 1, 2, 2, 3];
solution(5, arr1, arr2);

// function solution(a, b) {
//   let answer = "";
//   for (let i = 0; i < a.length; i++) {
//     if (a[i] === b[i]) answer += "D" + " ";
//     else if (a[i] === 1 && b[i] === 3) answer += "A" + " ";
//     else if (a[i] === 2 && b[i] === 1) answer += "A" + " ";
//     else if (a[i] === 3 && b[i] === 1) answer += "A" + " ";
//     else answer += "B" + " ";
//   }
//   return answer;
// }
