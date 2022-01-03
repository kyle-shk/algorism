// 정규식
function solution(s){
  let answer
      answer=s.replace(/A/gi,'#')
  return answer
}

let str="BANANA";
console.log(solution(str));

// function solution(s){
//   let answer="";
//   for(let x of s){
//       if(x=='A') answer+='#';
//       else answer+=x;
//   }
//   return answer;
// }

// let str="BANANA";
// console.log(solution(str));


// 개념
// 정규식: replace(/바뀔문자/g,바꿀문자)
// 특정단어를바꾸고싶을떄는 빈문자열을만들고 특정조건에서 바뀌는식으로 코드짠뒤 그외의값은 원래의문자가들어가게끔한다.