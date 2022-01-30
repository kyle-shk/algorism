function solution(b) {
  let n = b.length;
  // let answer = Array.from({ length: 5 }, () => 1);
  let answer = Array(5).fill(1)

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (b[j] > b[i]) answer[i]++;
    }
  }
  return answer;
}
console.log(solution([87,89,92,100,76]))


// Array.from과 화살표 함수 사용하기
// // Using an arrow function as the map function to
// // manipulate the elements
// Array.from([1, 2, 3], x => x + x);
// // [2, 4, 6]

// // Generate a sequence of numbers
// // Since the array is initialized with `undefined` on each position,
// // the value of `v` below will be `undefined`
// Array.from({length: 5}, (v, i) => i);
// // [0, 1, 2, 3, 4]

// 새로알게된개념
// 특정순위를 구할때는 미리 배열에 기초값을 넣어두고 조건을 만족했을때 배열의값들에 +1하는식으로 답을구하자
// 초기화배열을 만드는법은 Array.from({length:?},()=>넣고싶은값)