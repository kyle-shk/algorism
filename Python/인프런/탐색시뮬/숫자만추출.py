a=str(input())

def solution(a):
    answer = ''
    for i in range(len(a)):
        if a[i].isdigit() == True:
            answer += a[i]
    answer = int(answer)
    count=0
    for k in range(1,answer+1):
        if answer % k == 0:
            count +=1
    return answer,count

print(solution(a))