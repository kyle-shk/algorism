def solution(a,b,c):
    li=set()
    for i in range(a):
        for j in range(i+1,a):
            for k in range(j+1,a):
                li.add(c[i]+c[j]+c[k])
    li1=sorted(list(li),reverse=True)
    answer=li1[b-1]
    return answer

print(solution(10,3,[13,15,34,23,45,65,33,11,26,42]))