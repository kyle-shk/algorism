def solution(b):
    max = 0
    for i in b:
        sum=0
        tmp=i
        while tmp>0:
            sum+=tmp%10
            tmp=tmp//10
        if sum > max:
            max = sum
            answer = i
        elif sum == max:
            if(i>answer):
                answer = i
    return answer,max



print(solution([128,460,603,40,521,137,123]))