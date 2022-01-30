def solution(a):
    li=[]
    answer=[]
    for i in a:
        li.append(str(i)[::-1])
    for k in li:
        if int(k) == 1:
            continue
        for j in range(2,int(k)):
            if int(k) % j ==0:
                break
        else:
            answer.append(int(k))
    return answer

print(solution([32,55,62,3700,250]))
