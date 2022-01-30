# def solution(s, n):
#     low = "abcdefghijklmnopqrstuvwxyz" # 소문자. 인덱스는 0에서 25
#     up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     answer = ''
#     for char in s:
#         if char in low:
#             ind = low.find(char)+n # low 문자열에서 찾은 해당 알파벳 인덱스 + n
#             answer += low[ind%26] # 26으로 나눈 나머지를 사용할 경우 25를 초과하는 경우도 활용 가능
#         elif char in up:
#             ind = up.find(char)+n
#             answer += up[ind%26]
#         else: # 공백일 경우도 고려
#             answer += " "
#     return answer
     
# solution("a B z E", 4) # 'e F d I'

# https://data-science-blog.tistory.com/1


# def a(a,b):
#     for x in a:
#         if x in low:
#             ind=low.find(x)+n
#             answer+=low[ind%26]
#         elif char in up:
#             ind=low.find(x)+n
#             answer+=low[ind%26]
#         else:
#             answer += ''

# python and js index위치
# js: indexOf, python : find
# 안에있는지 확인
# python:find,js:includes


def solution(s, n):
    answer = ''
    low = "abcdefghijklmnopqrstuvwxyz" # 소문자. 인덱스는 0에서 25
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        if i == ' ':
            answer += ' '
            continue
        if low.find(i) >=0:
            Index=low.find(i)+n
            answer += low[Index%26]
        elif up.find(i)>=0:
            Index = up.find(i)+n
            answer += up[Index%26]
    return answer
print(solution('AB',1))