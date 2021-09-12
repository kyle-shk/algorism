// reduce를 최대최소문제에서 많이씀

// let a = [6,5,4,3,2];

// const reducerOne = (accumulator,currentvalue) => accumulator + currentvalue
// const reducerTwo = (accumulator,currentvalue) => accumulator - currentvalue
// const reducerThree = (accumulator,currentvalue) => accumulator > currentvalue ?
// accumulator : currentvalue
// const reducerFour = (accumulator,currentvalue) => accumulator < currentvalue ?
// accumulator : currentvalue

// console.log(a.reduce(reducerOne))
// console.log(a.reduce(reducerTwo))
// console.log(a.reduce(reducerThree))
// console.log(a.reduce(reducerFour))

let a = [10, 20, 30, 40, 50, 60];

const b = (accumulator, currentvalue) => {
  return accumulator + currentvalue;
};

console.log(a.reduce(b));
