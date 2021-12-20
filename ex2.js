function tri(a,b,c) {
    let max = Math.max(a,b,c);
    let sum = a+b+c;
    if(max<=sum-max) return 'YES';
    else return 'NO'
}
console.log(tri(6,7,11))