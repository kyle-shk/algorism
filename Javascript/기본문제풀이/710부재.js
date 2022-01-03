function solution(day, arr) {
  let answer = 0;

  for (let x of arr) {
    //일의자리를 가르키는법 -> 10으로나눠서 나온값이 일의 자리값임을 이용, 십의자리는 / 이용
    if (x % 10 == day) {
      answer++;
    }
  }
  return answer;
}

arr = [25, 23, 11, 47, 53, 17, 33];
console.log(solution(3, arr));
