// function solution(arr) {
//     // var answer = [];
//     var min = Number.MAX_SAFE_INTEGER;
//     var a
//     if(arr.length !== 1) {
//         for(let i=0;i<arr.length;i++) {
//             if(arr[i]<min) {
//                 min = arr[i]
//                 a=i
//             }
//         }
//         arr.splice(a,1)
//         return arr
//     } else {
//         return [-1]
//     }
//     // return answer;
// }
// console.log(solution([10]))

function solution(n) {
    // var answer =[]
    n=n.toString().split('').reverse()
    console.log(n)
    let b=n.map((a)=>{
       return parseInt(a)
    })
    return b
}
console.log(solution(12345))

// function solution(n) {
//     return n.toString().split('').reverse().map(o => parseInt(o));
// }

// console.log(solution(12345))