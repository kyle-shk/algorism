//반복문
let a = 1;
let b = 1;
for(var i=0;i<7;i++) {
    var c = a+b;
    a = b
    b = c
}
console.log(a)




function 피보나치(숫자) {
    if(숫자 ==1 || 숫자 == 2) {
        return 1
    }
    return 피보나치(숫자-1) + 피보나치(숫자-2)
}
console.log(피보나치(8))

// 피보나치(5) 피보나치(4) + 피보나치(3)
// 피보나치(4) 피보나치(3) + 피보나치(2)
// 피보나치(3) 피보나치(2) + 피보나치(1)
// 피보나치(2) 피보나치(1) 
// 피보나치(1)  1