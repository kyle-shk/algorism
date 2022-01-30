function solution(n, k, card){
    let answer;
    let tmp = new Set();
    // 3개로만들수있는 모든경우의수 코드(중복없음)
    for(let i=0; i<n; i++){
        for(let j=i+1; j<n; j++){
            for(let k=j+1; k<n; k++){
                tmp.add(card[i]+card[j]+card[k]);
            }
        }
    }
    // 배열기능을갖는것을만들때 array.from,내림차순은 function b-a
    let a=Array.from(tmp).sort((a, b)=>b-a);
    answer=a[k-1];
    return answer;
}

let arr=[13, 15, 34, 23, 45, 65, 33, 11, 26, 42];
console.log(solution(10, 3, arr));

// function solution(k,n,a){
//     let answer
//     let tep=new Set
//     for(let i=0;i<k;i++) {
//         for(let w=i+1;w<k;w++) {
//             for(let e=w+1;e<n;e++) {
//                 tep.add(a[i]+a[w]+a[e])
//             }
//         }
//     }
//     let a = Array.from(tep).sort((a,b)=>b-a)
//     answer = a[n-1]
//     return answer
// }