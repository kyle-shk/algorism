// function solution(a) {
//   //   let answer;
//   //   let mid = Math.floor(a.length / 2);
//   //   if (a.length % 2 == 1) answer = a.substr(mid, 1);
//   //   else answer = a.substr(mid - 1, 2);
//   //   return answer;

//   let answer;
//   let mid = Math.floor(a.length / 2);
//   if (a.length % 2 == 1) answer = a.substring(mid, mid + 1);
//   else answer = a.substring(mid - 1, mid + 1);
//   return answer;
// }
// console.log(solution("studym"));

// substirng, substr 개념정리

// 1. substr(시작인덱스,가져올문자열갯수)
// substr() 메서드는 문자열에서 특정 위치에서 시작하여 특정 문자 수 만큼의 문자들을 반환합니다.
// const str = 'Mozilla';

// console.log(str.substr(1, 2));
// // expected output: "oz"

// console.log(str.substr(2));
// expected output: "zilla"

// 2. substring(시작인덱스,종료인덱스(애는포함안됨))
// substring() 메소드는 string 객체의 시작 인덱스로 부터 종료 인덱스 전 까지 문자열의 부분 문자열을 반환합니다.
// const str = 'Mozilla';

// console.log(str.substring(1, 3));
// // expected output: "oz"

// console.log(str.substring(2));
// // expected output: "zilla"

function solution(a) {
  let num=''
  if(a.length%2 === 1) {
    num += a.substring(a.length/2,a.length/2+1)
  } else{
    num +=  a.substring(a.length/2-1,a.length/2+1)
  }
  return num;
}

console.log(solution("고구마건"));
