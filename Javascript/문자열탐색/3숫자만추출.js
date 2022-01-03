function solution(str){
    let answer="";
    let b = str.toUpperCase()
    for(let x of b) {
        let a =x.charCodeAt()
        if(a>=65 && a<=90) {
                continue;
        }
        else answer += x
    }
    let arr = answer.split('')

    if(arr[0] === '0') {
        arr.shift()
        answer=arr.join('')
        return answer
    } else {
        answer = arr.join('')
        return answer
    }
}

let str="g0en2T0s8eSoft";
console.log(solution(str));

// 강사님풀이
// function solution(str){
//     let answer="";
//     for(let x of str){
//         if(!isNaN(x)) answer+=x;
//     }  
//     return parseInt(answer);
// }

// let str="g0en2T0s8eSoft";
// console.log(solution(str));