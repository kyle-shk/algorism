var a = [10,20,30,1,2,3,4,5,7,9,4]

// a.sort() // 사전식 정렬
// console.log(a[a.length-1])

// console.log(Math.max(10,20))
// console.log(Math.min(10,20))

// console.log(Math.max.apply(null,a)) 1.메서드사용
// console.log(Math.min.apply(null,a))


// 2. 반복문 사용
let m = a[0]
for( var variable of a) {
    if(variable > m) {
        m = variable
    }
}
console.log(m)

let n = a[0]
for( var variable of a) {
    if(variable < n) {
        n = variable
    }
}
console.log(n)

