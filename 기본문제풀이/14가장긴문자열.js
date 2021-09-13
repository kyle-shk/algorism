function solution(b) {
  let answer,
    max = Number.MIN_SAFE_INTEGER;
  console.log("max : ", max);
  for (let x of b) {
    if (x.length > max) {
      max = x.length;
      answer = x;
    }
  }
  return answer;
}

console.log(solution(["teacherssaedas", "eweqweqwewqe", "asd"]));
