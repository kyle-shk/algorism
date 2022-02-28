def solution(a):
    # stack용도: (의 객를 세기위한 용도
    stack=[]
   
    sum=0
    
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(a[i])
        else:
            stack.pop()
           
            if a[i-1] == '(':
                sum+= len(stack)
            else:
                sum+=1
    return sum

word1 =input()
print(solution(word1))