function solution(a, b) {
  //   let answer = [];
  let count = 0;
  for (let i = 0; i < a; i++) {
    if (b[i + 1] > b[i]) {
      count++;
    }
  }
  return count;
}
let array = [130, 135, 148, 140, 145, 150, 150, 153];
console.log(solution(8, array));
