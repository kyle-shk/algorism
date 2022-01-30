function solution(a) {
  let answer;
  answer = a.filter(function (v, i) {
    if (a.indexOf(v) == i) return true;
  });
  return answer;
}
let c = ["good", "time", "good", "time", "studnet"];
console.log(solution(c));

// filter는 콜백함수가 참을 리턴한 그요소(만족하는 요소)들을 리턴해서 배열을만듬

