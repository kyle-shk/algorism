function solution(a, b) {
  let answer = [];
  for (let i = 0; i < a; i++) {
    if (b[i + 1] > b[i]) {
      answer.push(b[i + 1]);
    }
  }
  answer.unshift(b[0]);
  return answer;
}
// let array = [7, 3, 9, 5, 6, 12];
let array = [7, 11, 9, 15, 16, 2];
console.log(solution(6, array));
