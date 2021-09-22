function solution(a, b) {
  let count = 0;
  let max = 0;
  for (let i = 0; i < a; i++) {
    if (b[i] == 1) {
      count++;
      max += count;
    } else {
      count = 0;
    }
  }
  return max;
}
let array = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0];
console.log(solution(10, array));

//누적을한다는것은 특정 변수에 값을 누적하는걸의미
