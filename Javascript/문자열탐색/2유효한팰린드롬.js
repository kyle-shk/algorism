// function solution(s){
//     let answer="YES";
//     s=s.toLowerCase().replace(/[^a-z]/g, '');
//     if(s.split('').reverse().join('')!==s) return "NO";
//     return answer;
// }

// let str="found7, time: study; Yduts; emit, 7Dnuof";
// console.log(solution(str));

// 아스키코드이용
// 1.모든글자소문자로만듬 + 출력할yes변수만듬 -> 반복문을이용해 해당문자가 소문자인지확인 -> 확인하려면 해당문자를 아스키코드로 만들고
// 소문자의범위(97~122)에 있다면 해당글자를 빈문자열에 추가 -> 만들어진글자를 원래의 문자와 비교 -> 원래의문자를 배열로만든뒤
// ->reversed()함수로 글자를뒤집고 join()함수로 다시 문자열로만들어서 원래의 글자와 비교했을때 댜르면no 같다면 원래의 글자를 return하는식으로 코드작성
function solution(s) {
    let answer = 'YES';
    let res = '';
    s=s.toLowerCase();
    for(let x of s) {
        let num =x.charCodeAt();
        if(num>=97 && num<=122) res+= x
    }
    if(res.split('').reverse().join('') !== res) answer = "NO";
    return answer;
}

let str="found7, time: study; Yduts; emit, 7Dnuof";
console.log(solution(str));