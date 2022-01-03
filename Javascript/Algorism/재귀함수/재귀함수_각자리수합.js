// let result = 0;
// let x = '123123';
// while(true) {
//     if(x.length == 1) {
//         result += parseInt(x,10);
//         break;
//     }
//     let y = x.split('');
//     result += parseInt(y.pop(),10);
//     x=y.join('')

// }
// console.log(result)

// //재귀
// function 문자열역순(문자) {
//     if(문자.length == 1) {
//         return parseInt(문자,10)
//     }
//     return 문자열역순(문자.slice(0,문자.length-1)) + parseInt(문자[문자.length-1],10)
// }
// console.log(문자열역순('123123'));

function a(문자) {
    if ( Number(문자) < 10) {
        return 문자
    }
    return a(Math.floor(문자 / 10)) + Number(문자%10)
}
console.log(a('12345'))