// function solution(arr) {
//   let answer=[];
//   let sum=0,min=Number.MAX_SAFE_INTEGER;
//   for(let x of arr) {
//     // 1.홀수판별
//     if(x%2 ===1) {
//       // 2.홀수인것들의합
//       sum +=x;
//       // 3.홀수중 가장작은수판별
//       if(x<min) min=x;
//     }
//   }
//   answer.push(min)
//   answer.push(sum)
//   return answer
// }
// arr=[12,77,38,41,53,92,85];
// console.log(solution(arr))


function solution(day, arr){
  let answer=0;
  for(let x of arr) {
    if(x%10 === day) answer++
  }
  return answer
}

arr=[25, 23, 11, 47, 53, 17, 33];
console.log(solution(3, arr));