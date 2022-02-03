def solution(num,a):
    largest = -12341251
    # 가로,세로
    # 행선택
    for i in range(num):
        # 새로운행일때 기존의합 초기화
        sum1=sum2=0
        # 열선택
        for j in range(num):
            sum1+=a[i][j]
            sum2+=a[j][i]
        if sum1>largest:
            largest=sum1
        if sum2>largest:
            largest = sum2
    # 대각선
    sum1=sum2=0
    for i in range(num):
        sum1 += a[i][i]
        sum2 += a[i][num-i-1]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest = sum2
    return largest

arr= [
    [10,13,10,12,15],
    [12,39,30,23,11],
    [11,25,50,53,15],
    [19,27,29,37,27],
    [19,13,30,13,19]
    ]   
print(solution(5,arr))