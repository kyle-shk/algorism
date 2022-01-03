let result = "10 9 8 7 6 5 4 3 2 1";

// let b = a.split(" ");
// let c = Math.max.apply(null, b);
// console.log(c);

result = result.split(" ").map((n) => {
  return parseInt(n, 10);
});
// console.log(result);

result.sort((a, b) => {
  return b - a;
});
console.log(result[0]);
