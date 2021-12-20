function cal(a) {
  let sum = 0; //undefiend + 0 = nan
  for (let i = 1; i <= a; i++) {
    sum += i;
    console.log("sum : ", sum);
  }
  return sum;
}

console.log(cal(6));
