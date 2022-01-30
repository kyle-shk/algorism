function solution(arr) {
  let answer = Number.MIN_SAFE_INTEGER;
  let n = arr.length;
  // let sum1 = (sum2 = 0);
  for (let i = 0; i < n; i++) {
    let sum1 = sum2 = 0;
    for (let j = 0; j < n; j++) {
      sum1 += arr[i][j];
      sum2 += arr[j][i];
    }
    answer = Math.max(answer, sum1, sum2);
  }
  sum1 = sum2 = 0;
  for (let i = 0; i < n; i++) {
    sum1 += arr[i][i];
    sum2 += arr[i][n - i - 1];
  }
  answer = Math.max(answer, sum1, sum2);
  return answer;
}
let arr = [
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19],
];
console.log(solution(arr));

// let answer = Number.MIN_SAFE_INTEGER을 해주는 이유?

// answer는 최종적으로 제일 큰 값을 저장하는 변수이므로 초기화를 제일 작은 값으로 해서
// 최초 Math.max(answer, sum1, sum2) 비교시 answer값은 무시(sum1, sum2보다 당연히 작으므로)되고,
// sum1, sum2 중 큰 값이 answer가 되도록하기 위함입니다.

//필요지식
//행,열 의 누적합 -> 이중배열
// 대각선의 누적합 -> 이중배열

// 1.가로,세로,대각성의누적합을 구해야함
// 2.최대의값을 구해야하기때문에먼저 가장작은값으로 초기화
// 3.가로와 세로의 합을 이중배열로 구함
// 4.대각선들의 합을 반복문으로 구함