function solution(a) {
  let answer = [];
  let b = a.split("");
  //   console.log("b : ", b);
  for (let i = 0; i < b.length; i++) {
    if (b[i] === "A") {
      let c = b[i].replace(b[i], "#");
      answer.push(c);
    } else {
      answer.push(b[i]);
    }
  }
  let d = answer.join("");
  console.log(d);
}

// console.log(solution("BANANA"));
solution("BANANA");

//2.문자열이용

// function solution(s) {
//   let answer = "";
//   for (let x of s) {
//     if (x === "A") answer += "#";
//     else answer += x;
//   }
//   return answer;
// }
// let str = "BANANA";
// console.log(solution(str));
