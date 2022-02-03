def solution(num,a):
    count=0
    for i in range(1,num+1):
        for j in range(1,num+1):
            if a[i][j] > a[i-1][j] and a[i][j] > a[i][j+1] and a[i][j] > a[i+1][j] and a[i][j] > a[i][j-1]:
                count+=1
            else:
                continue
    return count
arr=[
    [0,0,0,0,0,0,0],
    [0,5,3,7,2,3,0],
    [0,3,7,1,6,1,0],
    [0,7,2,5,3,4,0],
    [0,4,3,6,4,1,0],
    [0,8,7,3,5,2,0],
    [0,0,0,0,0,0,0]
]
print(solution(5,arr))