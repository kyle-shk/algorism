function solution(n) {
    var answer = 0;
    if((Math.sqrt(n))===Math.floor(Math.sqrt(n))) {
        answer += (Math.sqrt(n) +1) ** 2
    }
    else {
        answer += -1
    }
    return answer;
}
console.log(solution(3))