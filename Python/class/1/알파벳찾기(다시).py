# n = input()
# abc = 'abcdefghijklmnopqrstuvwxyz'

# for i in abc:
#     if i in n:
#         print(n.index(i), end=' ')
#     else:
#         print(-1, end=' ')

# https://gururuglasses.tistory.com/88

# 아스키코드로풀기
# a~z는 97~122임
word = input()
alpabet = list(range(97, 123))
for x in alpabet:
    print(word.find(chr(x)), end=' ')
# https://ooyoung.tistory.com/68
# 아스키 https://j-remind.tistory.com/55
