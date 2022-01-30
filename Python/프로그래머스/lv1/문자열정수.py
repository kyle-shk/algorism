# def solution(s):
#     answer = 0
    
#     answer += int(s)
#     return answer
# print(solution('-1234'))

def solution(n):
    answer = ''
    for i in range(n):
        if i%2 ==0:
            answer += '수'
        else:
            answer += '박'
    return answer
print(solution(3))