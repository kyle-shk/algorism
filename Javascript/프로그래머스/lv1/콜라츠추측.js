function solution(num) {
    var answer = 0;
    while(num !== 1) {
        if(num %2 ===0) {
            num=Math.floor(num /2)
            answer++
        } else if (num %2 !== 0) {
            num=Math.floor((num*3)+1)
            answer++
        }
        if(answer === 500) {
            return answer=-1
        }
    }
    return answer;
}
console.log(solution(626331))