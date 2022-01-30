// function solution(n, arr){
//     let answer, max=Number.MIN_SAFE_INTEGER;
//     for(let x of arr) {
//         let sum=0,tmp=x;
        // while(tmp) {
        //     sum+=(tmp%10);
        //     tmp=Math.floor(tmp/10)
        // }
//         if(sum>max) {
//             max = sum;
//             answer=x;
//         }
        // else if (sum === max) {
        //     if(x>answer) answer=x;
        // }
//     }
//     return answer;
// }

// let arr=[128, 460, 603, 40, 521, 137, 123];
// console.log(solution(7, arr));


// reduce이용
function solution(n, arr){
    let answer, max=Number.MIN_SAFE_INTEGER;
    for(let x of arr) {
        let sum= String(x).split('').reduce((a,b)=>a+Number(b),0) //toString으로도 문자열만들수있음
        if(sum>max) {
            max = sum;
            answer=x;
        }
        else if (sum === max) {
            if(x>answer) answer=x;
        }
    }
    return answer;
}

let arr=[128, 460, 603, 40, 521, 137, 123];
console.log(solution(7, arr));

// 개소리
// function a1(a,arr) {
//     let sum=0
//     let max = Number.MIN_SAFE_INTEGER;
//     for(let i of arr) {
//         for(let j=0;j<String(i).length;j++) {
//             sum += Number(String(i)[j])
//         }
//         if(sum > max) {
//             max = sum
//         }
//         sum=0
//     }
//     return max
// }
// let arr=[128, 460, 603, 40, 521, 137, 123];
// console.log(a1(7, arr));

// 구하려는것:배열안에있는 각 원소들의합
// how? : 배열안에있는 원소들을 하나씩 꺼내고 -> 원소들의 원소를 각각 더한다 
// how? : 배열안에있는 수는 숫자이므로 먼저 문자열로 속성을 바꾼다 -> 이유는 원소들의 원소를 배열로 나눌려고 -> 원소단위로 접근하기위해
// 한원소기준 하나의 배열이 나오니까 reduce함수를 이용해 각원소들의 누적값을 구하자 -> 누적값초기는 0으로설정하고 순회하는배열들은 현재 문자열이니 Number로 속성을바꾸고 처리한다
