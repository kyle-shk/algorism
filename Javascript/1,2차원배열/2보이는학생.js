function solution(b) {
  let answer=1;
  let max=b[0];
  for(let i=1;i<b.length;i++) {
    if(max<b[i]) {
      answer++
      max=b[i]
  }
}
  return answer;
}
let array = [130, 135, 148, 140, 145, 150, 150, 153];
console.log(solution(array));
