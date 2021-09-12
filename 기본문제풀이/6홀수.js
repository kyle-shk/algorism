function odd(a) {
  let sum = 0;

  for (let i = 0; i < a.length; i++) {
    if (a[i] % 2 !== 0) {
      sum += a[i];
    }
  }

  return sum;
}
function small(b) {
  let min = Number.MAX_SAFE_INTEGER;
  let a;
  //   console.log("min : ", min);
  for (let i = 0; i < b.length; i++) {
    if (b[i] % 2 != 0) {
      a = b[i];
      //   console.log("b: ", a);
      if (a < min) {
        // ????
        min = a;
        // console.log("min11 : ", min); //???
      }
    }
  }
  return min;
}
// function small(b) {
//   let min = Math.max(...b);
//   let a;
//   for (let i = 0; i < b.length; i++) {
//     if (b[i] % 2 != 0) {
//       a = b[i];
//       if (a < min) {
//         min = a;
//       }
//     }
//   }
//   return min;
// }
// function small(b){
//     let min = Infinity;
//     let a;
//     for (let i=0; i<b.length;i++){
//         if(b[i]%2 != 0){
//             a = b[i];
//             if ( a< min){
//                 min = a
//             }
//         }
//     }
//     return min
// }
console.log("small", small([12, 77, 38, 41, 53, 92, 85]));
console.log("odd", odd([12, 77, 38, 41, 53, 92, 85]));

function odd(a) {
  let sum = 0;

  for (let i = 0; i < a.length; i++) {
    if (a[i] % 2 !== 0) {
      sum += a[i];
    }
  }

  return sum;
}
function small(b) {
  let min = Infinity;
  let a;
  for (let i = 0; i < b.length; i++) {
    if (b[i] % 2 != 0) {
      a = b[i];
      if (a < min) {
        min = a;
      }
    }
  }
  return min;
}
console.log("small", small([12, 77, 38, 41, 53, 92, 85]));
console.log("odd", odd([12, 77, 38, 41, 53, 92, 85]));
