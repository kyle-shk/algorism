function solution(arr) {
  let answer = arr;
  let sum = arr.reduce((a, b) => {
    return a + b;
  }, 0); //누적값
  console.log("sum1 : ", arr);
  console.log("sum2 : ", sum);
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      //   console.log("i :", arr[i], "j :", arr[j]);
      if (sum - (arr[i] + arr[j]) === 100) {
        arr.splice(i, 1);
        arr.splice(j - 1, 1); // j,i로 바꿔도 가능
      }
    }
  }

  //   console.log("sum : ", sum);
  console.log(answer);
  //   return answer;
}

let arr = [20, 7, 23, 19, 10, 15, 25, 8, 13];
solution(arr);
