function solution(x) {
    var answer = true;
    x=x.toString().split('')
    let sum=0;
    for (let a of x){
        sum += Number(a)
    }
    if(Number(x.join('')) % sum !==0) {
        answer = false;
    }
    return answer;
}
console.log(solution(11))