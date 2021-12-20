function solution(b) {
  let n = b.length;
  let answer = Array.from({ length: 5 }, () => 1);
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (b[j] > b[i]) answer[i]++;
    }
  }
  return answer;
}



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
