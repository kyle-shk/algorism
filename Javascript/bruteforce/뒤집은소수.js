// 소수판별 함수
// function isPrime(num){
//     if(num===1) return false;
//     // 16을기준으로 16의제곱근인 4까지만 확인하면됨 왜냐하면 그뒤로는 앞부분의반복
//     for(let i=2; i<=parseInt(Math.sqrt(num)); i++){
//         if(num%i===0) return false;
//     }
//     return true;
// }
// function solution(arr){
//     let answer=[];
//     for(let x of arr){
//         let res=0;
//         while(x){
//             let t=x%10;
//             res=res*10+t;
//             x=parseInt(x/10);
//         }
//         if(isPrime(res)) answer.push(res);
//     }
//     return answer;
// }

// let arr=[32, 55, 62, 20, 250, 370, 200, 30, 100];
// console.log(solution(arr));

// 배열이용
// function isPrime(num){
//     if(num===1) return false;
//     for(let i=2; i<=parseInt(Math.sqrt(num)); i++){
//         if(num%i===0) return false;
//     }
//     return true;
// }
function solution(arr){
    let answer=[];
    for(let x of arr){
        let res=Number(x.toString().split('').reverse().join(''));
        for(let i=2;i<Math.sqrt(res)+1;i++) {
            if (res === 1) {
                continue
            }
            if (res % i ===0) {
                break
            }
            answer.push(res)
            break
        }
    }
    return answer;
}

let arr=[32, 55, 62, 20, 250, 370, 200, 30, 100];
console.log(solution(arr));