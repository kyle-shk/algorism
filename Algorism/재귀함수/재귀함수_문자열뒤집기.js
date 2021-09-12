// 문자열 뒤집기
let result = '';
let x = 'kimshinhyup';
while(true) {
    if(x.length == 1) {
        result += x;
        break
    }
    let y = x.split('');
    console.log(y)
    result += String(y.pop());
    console.log('result: ',result)
    x = y.join('') //1개남은상태
    console.log('x : ',x )
}
console.log(result)

//재귀함수
// function 문자열역순(문자) {
//     if (문자.length == 1) {
//         return 문자
//     }
//     console.log(문자.slice(0,문자.length-1));
//     return 문자[문자.length-1] + 문자열역순(문자.slice(0,문자.length-1))
// }
// console.log(문자열역순('kimshinhyup'))

//문자열열역순('leehojun')  'n' + 문자열열역순('leehoju') ->nujoheel
//문자열열역순('leehoju')   'u' + 문자열열역순('leehoj')
// 문자열열역순('leehoj')  'j' + 문자열열역순('leeho') ->joheel
// 문자열열역순('leeho')  'o' + 문자열열역순('leeh') -> oheel
// ...
//문자열열역순('le')      'e' + 문자열열역순('l') -> el
//문아열열역순('l')       'l'






// function 문자뒤집기(a) {
//     if ( a.length == 1) {
//         return a
//     }
//     return a[a.length-1] + 문자뒤집기(a.slice(0,a.length-1))
// }

// console.log(문자뒤집기('kimshin'))