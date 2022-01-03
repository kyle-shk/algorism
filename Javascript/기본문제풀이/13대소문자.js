// function solution(a) {
//   let answer = [];
//   let b = a.split("");
//   for (let i in b) {
//     if (b[i] === b[i].toUpperCase()) {
//       b[i] = b[i].toLowerCase();
//       answer.push(b[i]);
//     } else {
//       b[i] = b[i].toUpperCase();
//       answer.push(b[i]);
//     }
//   }
//   let c = answer.join("");
//   return c;
// }
// console.log(solution("StuDY"));
// console.log(solution("STUDYmate"));
function solution(a) {
  let answer ='';
  for(let x of a) {
    if(x===x.toUpperCase()) answer += x.toLowerCase()
    else answer += x.toUpperCase()
  } 
  return answer
}
console.log(solution("StuDY"));
console.log(solution("STUDYmate"));
