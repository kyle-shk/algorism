// function solution(s){
//     let answer="YES";
//     s=s.toLowerCase().replace(/[^a-z]/g, '');
//     if(s.split('').reverse().join('')!==s) return "NO";
//     return answer;
// }

// let str="found7, time: study; Yduts; emit, 7Dnuof";
// console.log(solution(str));

// 아스키코드이용
function solution(s) {
    let answer = 'YES';
    let res = '';
    s=s.toLowerCase();
    for(let x of s) {
        let num =x.charCodeAt();
        if(num>=97 && num<=122) res+= x
    }
    if(res.split('').reverse().join('') !== res) answer = "NO";
    return answer;
}

let str="found7, time: study; Yduts; emit, 7Dnuof";
console.log(solution(str));