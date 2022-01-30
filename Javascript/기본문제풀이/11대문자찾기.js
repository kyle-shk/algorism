// function solution(a) {
//   let count = 0;
//   let c = a.split("");
//   for (let i in c) {
//     if (c[i].toUpperCase() === c[i]) {
//       count++;
//     }
//   }
//   return count;
// }
// console.log(solution("KoreaTimeGood"));

// function solution(a) {
//   let count = 0;
//   // let c =  ''
//   for (let i of a) {
//     if (i.toUpperCase() === i) {
//       count++;
//     } 
//   }
//   return count;
// }
// console.log(solution("KoreaTUmeGood"));


// 아스키코드
// 대문자:65~90, 소문자:97~112

function solution(a) {
  let count = 0;
  for (let i of a) {
    let num = i.charCodeAt()
      if (num >=65 && num <=90) {
      count++;
    } 
  }
  return count;
}
console.log(solution("KoreaTUmeGood"));