function cal(a, b, c) {
  let answer;
  if (a < b) {
    answer = a;
  } else {
    answer = b;
  }
  // if (c < answer) {
  //   answer = c;
  // }
  if (answer < c) {
    console.log(answer);
  }
  console.log(answer);
}
cal(11, 5, 2);
