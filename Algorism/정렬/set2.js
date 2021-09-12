const p = {
  김: "010",
  신: "200",
  협: "23",
  나: "ㅂㄷ",
  김: "010",
  신: "200",
  바: "123",
  나: "ㅂㄷ",
};
let result = new Set();

for (let i in p) {
  result.add(p[i]);
}
console.log(result);
