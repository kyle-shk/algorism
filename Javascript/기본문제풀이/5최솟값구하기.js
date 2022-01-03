// function a(a) {
//   //spread operator 이용
//   return Math.min(...a);
//   // Math.min.apply(null,a)
// }
function solution(arr) {
  let answer,min=Number.MAX_SAFE_INTEGER;
  for(let i=0;i<arr.length;i++) {
    if(arr[i]<min) min = arr[i]
    answer = min
  }
  return answer
}

console.log(solution([5, 3, 7, 11, 2, 15, 17]));
