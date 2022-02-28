def solution(array, commands):
    answer = []
    li=[]
    for a,b,c in commands:
        li+=array[a-1:b]
        li.sort()
        answer.append(li[c-1])
        li=[]
    return answer

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array,commands))

# https://velog.io/@chaegil15/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A0%95%EB%A0%AC-K%EB%B2%88%EC%A7%B8%EC%88%98
# def solution(array, commands):
#     answer = []
#     for i in range(len(commands)):
#         arr = array[commands[i][0]-1:commands[i][1]]
#         arr.sort()
#         answer.append(arr[commands[i][2]-1])
#     return answer