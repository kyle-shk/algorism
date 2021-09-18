function solution(a) {
  let answer;
  answer = a.filter(function (v, i) {
    if (a.indexOf(v) == i) return true;
  });
  return answer;
}
let c = ["good", "time", "good", "time", "studnet"];
console.log(solution(c));
