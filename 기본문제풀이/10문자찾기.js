// function solution(a, b) {
//   let count = 0;
//   let c = a.split("");
//   // for(let s of x) {if(x ===t) count++}
//   for (let i = 0; i < a.length; i++) {
//     if (c[i] === b) {
//       count++;
//     }
//   }
//   return count;
// }
//매개변수로 전달받은 문자열을 배열로만듬 왜? -> 배열에 있는 원소하나하나 비교해서 값비교하려고
//count라는 변수를 만들고 조건이 성립했을떄 +1 하는식으로 전개

// console.log(solution("COMPUTERPROGRAMMING", "R"));

function solution(s, t){
  let answer=0;
  for(let x of s){
      if(x===t) answer++;
  }
  return answer;
}

let str="COMPUTERPROGRAMMING";
console.log(solution(str, 'R'));