function solution(s){
    let answer="YES";
    let a = s.toLowerCase()
    for(let i=0;i<s.length;i++) {
        if(a[i] === a[s.length-i-1]) continue
        else answer = 'NO'
    }
    return answer;
}

let str="go1og";
console.log(solution(str));

// function solution(s){
//     let answer="YES";
//     s=s.toLowerCase();
//     let len=s.length;
//     for(let i=0; i<Math.floor(len/2); i++){
//         if(s[i]!=s[len-i-1]) return "NO";
//     }
//     return answer;
// }

// let str="goooG";
// console.log(solution(str));

// reverse()메서드 사용
// function solution(s){
//     let answer="YES";
//     s=s.toLowerCase();
//     if(s.split('').reverse().join('')!=s) return "NO";    
//     return answer;
// }

// let str="gooG";
// console.log(solution(str));