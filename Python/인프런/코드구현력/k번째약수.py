def solution(a,b):
    li=[]
    for i in range(1,a+1):
        if a % i == 0:
            li.append(i)
        else:
            return -1
    return li[b-1]
print(solution(6,5))
