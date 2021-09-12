function solution(a) {
  let count = 0;
  let c = a.split("");
  for (let i in c) {
    if (c[i].toUpperCase() === c[i]) {
      count++;
    }
  }
  return count;
}
console.log(solution("KoreaTimeGood"));
