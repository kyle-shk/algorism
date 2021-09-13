// function solution(s) {
//   let answer = "";
//   for (let i = 0; i < s.length; i++) {
//     // console.log(s[i], i, s.indexOf(s[i]));
//     if (s.indexOf(s[i]) == i) answer += s[i];
//   }
//   return answer;
// }
// console.log(solution("ksekkset"));

//특정문자의 갯수
function solution(s) {
  let answer = 0;
  //   let pos = s.indexOf("k");
  //   while (pos !== 1) {
  //     answer += 1;
  //     pos = s.indexOf("k", pos + 1);
  //   }
  //for문이용
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "k") {
      answer += 1;
    } else {
      continue;
    }
  }
  return answer;
}
console.log(solution("ksekkset"));

// indexOf() 함수
// 특정 문자 위치 찾기
// string.indexOf(searchvalue, position)
// indexOf 함수는, 문자열(string)에서 특정 문자열(searchvalue)을 찾고,
// 검색된 문자열이 '첫번째'로 나타나는 위치 index를 리턴합니다.
// 파라미터
// searchvalue : 필수 입력값, 찾을 문자열
// position : optional, 기본값은 0, string에서 searchvalue를 찾기 시작할 위치
// 찾는 문자열이 없으면 -1을 리턴합니다.
// 문자열을 찾을 때 대소문자를 구분합니다.

//예제
// const str = "abab";

// document.writeln(str.indexOf('ab')); // 0
// document.writeln(str.indexOf('ab', 1)); // 2

// 예제 2
// position 값을 '1' 로 입력하였습니다.
// 위 예제에서는 'abab' 문자열의 1번째 index부터 'ab' 문자열을 검색하므로,
// index 0에 있는 'ab'는 무시합니다

// 출처: https://hianna.tistory.com/379 [어제 오늘 내일]

//문제 푸는순서
//공통된문자을 찾아야한다
//공통된문자란 처음나오는 문자의위치와  해당문자의 인댁스가 같은걸 말한다
//이걸확인하려면 for문반복을 이용해 해당문자의 위치와 ㅑndexOf를 이용해 해당문자의 위치인덱스를 구해서 비교하자
//해당위치 인데스와 Indexof로나온값이 다르면 그 값은 제가하자
//처음에 일반 문자열을 만들고 조건에맞는(if (s.indexof(문자열위치))==s[i]) 가 같은애들만 문자열에더하자))
