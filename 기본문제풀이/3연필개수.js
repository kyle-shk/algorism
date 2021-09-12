function pen(a) {
  let p = 12;
  let answer;
  if (a % p < 1) {
    answer = a / p;
  } else {
    answer = a / p + 1;
  }
  return answer;
}

console.log(Math.floor(pen(178)));

//강사님 풀이

// function solution(n) {
//     let answer = = Math.ceil(n/12)
//     return answer
// }
