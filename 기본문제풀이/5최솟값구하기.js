function a(a) {
  //spread operator 이용
  return Math.min(...a);
  // Math.min.apply(null,a)
}

console.log(a([5, 3, 7, 11, 2, 15, 17]));
