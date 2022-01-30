function solution(n) {
    var answer = 0;
    // n=n.toString().split('')
    // console.log(n)
    for(let i=1;i<=Number(n);i++) {
        if(n%i === 0) {
            answer += i
            // console.log(answer)
        }
    }
    return answer;
}
console.log(solution(12))