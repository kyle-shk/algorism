word = input().lower()
word_list = list(set(word))
cnt = []
for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_list[(cnt.index(max(cnt)))].upper())
# 처음에 각문자에 해당하는 갯수를 리스트에넣어줌
# 반복문순으로 갯수리스트에 해당하는 문자를넣었으므로 같은위치의 갯수리스트원소와 문자열인덱스는 서로 같은것임
# 만일 숫자리스트의 가장큰값의갯수가 2이상이면 ?출력
# 그게아니면 문자열리스트중 숫자리스트의원소중가장큰 원소의 인덱스를가져와 문자열인덱스에넣어주면 가장많은숫자를가진 문자열을 출력할수있음

# https://wook-2124.tistory.com/257
