// 잘못된 난쟁이고를떄
// function solution(arr){
//     let answer=[]
//     let sum=arr.reduce((a,b)=>a+b)
//     for(let i=0;i<arr.length-1;i++) {
//         for(let j=i+1;j<arr.length;j++) {
//             if(sum-(arr[i]+arr[j]) === 100) {
//                 answer.push(arr[i])
//                 answer.push(arr[j])
//             }
//         }
//     }
//     console.log(sum)
//     return answer;
// }

// let arr=[20, 7, 23, 19, 10, 15, 25, 8, 13];
// console.log(solution(arr));

//제대로된값
// 핵심은 전체에서 특정 두명의난쟁이를골라 뺐을때 100이된다면 지칭된2명의난쟁이를 배열에서빼면 답임
function solution(arr){
    let answer=arr;
    // 1.전체배열의합을구함
    let sum=arr.reduce((a,b)=>a+b)
    // 2.이중반복문을 통해 제거될 난쟁이쌍을 구함
    for(let i=0;i<arr.length-1;i++) {
        for(let j=i+1;j<arr.length;j++) {
            // 3.전체에서 지목된난쟁이한쌍을 뺴서 100이되면 지칭된난쟁이를 배열에서 제거하는코드를작성
            if(sum-(arr[i]+arr[j]) === 100) {
             arr.splice(j,1)
             arr.splice(i,1)
            }
        }
    }
    // console.log(sum)
    return answer;
}

let arr=[20, 7, 23, 19, 10, 15, 25, 8, 13];
console.log(solution(arr));