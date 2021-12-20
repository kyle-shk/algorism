function solution(...s) {
  var answer = true;
  var a = s[0].split("");
  if (a.length !== 4 || a.length !== 6) {
    answer = false;
    return answer;
  }
  for (let i = 0; i < a.length; i++) {
    if (isNaN(a[i]) == false) {
      return answer;
    } else {
      answer = false;
      return answer;
    }
  }
}

console.log(solution("a234"));
