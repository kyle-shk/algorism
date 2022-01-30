def solution(a,b):
    avg=round(sum(b)/a)
    min=float('inf')
    for idx,x in enumerate(b):
        tmp = abs(x-avg)
        if min>tmp:
            min = tmp
            score = x
            res = idx+1
        elif min == tmp:
            if x> score:
                score = x
                res = idx+1
    return avg,res


print(solution(10,[45,73,66,87,92,67,75,79,75,80]))