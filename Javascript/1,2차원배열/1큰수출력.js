function solution(b) {
  let arr=[]
  arr.push(b[0])
  for(let i=1;i<b.length;i++) {
    if(b[i]<b[i+1]) {
      arr.push(b[i+1])
    }
  }
  return arr
}
let array = [7, 3, 9, 5, 6, 12];
// let array = [7, 11, 9, 15, 16, 2];
console.log(solution(array));
