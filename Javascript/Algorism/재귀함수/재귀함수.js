//재귀함수
// 내가 나를 호출하는 함수

// 반복문 <-> 재귀함수

// 반복 -> 밑에서 위로
// s+= 1
// s+= 2
// s+= 3
// ...
// s+= 100
let s = 0;
for (var i=0;i< 101; i++) {
    s += i;
}

console.log(s)

let m =1;
for(var i=1;i<6;i++) {
    m *= i;
}

console.log(m)
// 재귀함수 -> 위에서 아래로
// 순번     f(n)     n    return     최종
// 1       f(100)  100   100 + f(99)  100+99+98....+1
// 2       f(99)   99    99 + f(98)   99+98+...+1
//3        f(98)   98    98 + f(97)   98+....+1
// ...
// 2       f(2)     2     2 + f(1)     2+1
// 1       f(1)     1      1           


function f(n) {
    if (n<=1) {
        return 1
    }
    return n + f(n-1)
} 

//console.log(f(100))

// 순번     f(n)     n    return     최종
// 1       f(5)    5     5 * f(4)   5*24
// 2       f(4)   4    4 * f(3)     4*6
//3        f(3)   3     3 * f(2)    3*2
//2       f(2)     2     2 * f(1)    2*1
//1       f(1)     1       1

function f(n) {
    if(n<=1) {
        return 1
    }
    return n * f(n-1)
}
console.log(f(5))

//