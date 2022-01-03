function tri(a, b, c) {
  let answer, max;
  console.log("answer1", typeof answer);
  let sum = a + b + c;
  if (a < b) {
    max = b;
  } else {
    max = a;
  }
  if (max < c) {
    max = c;
  }
  //가장긴 막대구하기
  if (sum - max <= max) {
    answer = "no";
  } else {
    answer = "yes";
  }
  //짧은 두변의길이의 합이 긴 변의 길이 보다 커야 삼각형 성립
  return answer;
}
console.log("a", tri(6, 7, 11));

console.log("b", tri(13, 3, 17));
