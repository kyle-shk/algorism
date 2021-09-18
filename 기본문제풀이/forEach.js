//forEach,map,filter,reduce -> 고차함수 즉 매개변수에 함수를 전달받아야함
// 함수를 받아야함 , 함수내부에서 실행될것들(생략해도가능), for반복문 대신해서 사용
// function forEach(predicate, thisArg) {
//a는 배열
//   for (let i = 0; i < a.length; i++) {
//     predicate(a[i], i); //콜백함수 호출문, 위의 함수는 뇌피셜
//   }
// }
//forEach
// a = [10, 11, 12, 13, 14, 15]; //v는 배열의 요소들 ,i는 배열의 인덱스
// a.forEach(
//   function (v, i) {
//     console.log(v, i, this);
//   },
//   [1, 2]
// );

//map 새로운 배로운 만듬

//내부
// function map(predicate, thisArg) {
//   let list = [];
//   for (let i = 0; i < a.length; i++) {
//     list.push(predicate(a[i]), i);
//   }
//  return list
// }
//기본예제
// a = [10, 11, 12, 13, 14, 15];
// let answer = a.map(function (v) {
//   return v * v;
// });
// console.log(answer);

//map은 새로운 배열과 원본배열의 길이가 무조건같아야하므로 조건식이있을때 조건이일치하지않으면 undefiend를 리턴함
// a = [10, 11, 12, 13, 14, 15];
// let answer = a.map(function (v, i) {
//   if (v % 2 == 0) return v;
// });
// console.log(answer);

// //filter
// 새로운배열을 생성함 그러나 map이랑 다르게 굳이 새로운 배열의 길이가 원본배열과 같을 필요는 없음
//,정확하게 원하는 원소만 배열을 생성해서 리턴함
//내부
// function map(predicate, thisArg) {
//   let list = [];
//   for (let i = 0; i < a.length; i++) {
//     if ((predicate(a[i]), i)) list.push(a[i]);
//   }
//   return list;
// }

// a = [10, 11, 12, 13, 14, 15];
// let answer = a.filter(function (v, i) {
//   if (v % 2 == 1) return v;
// });
// console.log(answer);

//reduce
//배열이아닌 어떤값을 생성해서 리턴
// function reduce(predicate, value) {
//   let result = value;
//   for (let i = 0; i < a.length; i++) {
//     result = predicate(result, a[i]);
//   }
//   return result;
// }

// a = [10, 11, 12, 13, 14, 15];
// //누적,배열
// let answer = a.reduce(function (acc, value) {
//   return acc + value;
// }, 0);
// console.log(answer);
