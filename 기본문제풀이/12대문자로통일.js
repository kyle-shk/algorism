// function solution(a) {
//   let answer = [];
//   let b = a.split("");
//   for (let i in b) {
//     if (b[i].toUpperCase() == b[i]) {
//       answer.push(b[i]);
//     } else {
//       b[i] = b[i].toUpperCase();
//       answer.push(b[i]);
//     }
//   }
//   let answers = answer.join("");
//   return answers;
// }
// console.log(solution("ItisTimeTiStudy"));

//문자열로풀기
function solution(a) {
  let answer = "";
  for (let i of a) {
    if (i === i.toLowerCase()) {
      answer += i.toUpperCase();
    } else {
      answer += i;
    }
  }

  return answer;
}
console.log(solution("ItisTimeTiStudy"));
