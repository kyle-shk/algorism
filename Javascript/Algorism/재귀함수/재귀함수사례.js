//사례 - 2진수 변환
// Math.ceil() : 소수점 올림, Math.floor() : 소수점 버림 , Math.round() : 소수점 반올림
let result = ''
let x = 11;
while(true) {
    if(x%2 == 0) {
        result += '0' // result = '0' + result;
    } else {
        result += '1' // result = '1' + result;
    }
    x = Math.floor(x/2)
    if( x == 1) {
        result += String(x) // result = String(x) + result;
        break
    }
}
console.log(result.split('').reverse().join(''))

// function 이진법(숫자) {
//     if(숫자 == 1 || 숫자 == 0) {
//         return String(숫자);
//     }
//     return 이진법(Math.floor(숫자/2)) + String(숫자%2)
// }
// console.log(이진법(11));

// 이진법(11)    이진법(5) + Sting(1)
// 이진법(5)     이진법(2) + String(1)
// 이진법(2)     이진법(1) + String(0)
// 이진법(1)      

function f(n) {
    if ( n==1) {
        return String(n)
    }
    return f(Math.floor(n/2)) + String(n%2)
}

console.log(f(11))