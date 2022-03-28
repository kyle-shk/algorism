def solution(a,b):
    b.sort()
    start = 0
    end = len(b)-1
    while start<=end:
        mid = (start+end)//2
        if a == b[mid]:
            return mid
        elif a>b[mid]:
            start = mid+1
        else:
            end = mid-1

    return -1
arr=[23,87,65,12,57,32,99,31]
print(solution(32,arr))
