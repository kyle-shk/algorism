from this import d


def solution(arr):
    cnt=0
    for i in range(7):
        for j in range(3):
            if arr[i][j] == arr[i][j+4] and arr[i][j+1] == arr[i][j+3]:
                cnt+=1
            if arr[j][i] == arr[j+4][i] and arr[j+1][i] == arr[j+3][i]:
                cnt+=1
    return cnt
# https://velog.io/@jiffydev/algo-21

# def solution(arr):
#     cnt=0
#     # 가로
#     for i in range(3):
#         for j in range(7):
#             answer=arr[j][i:i+5]
#             if answer == answer[::-1]:
#                 cnt+=1
#             for k in range(2):
#                 if arr[i+k][j] != arr[i+5-k-1][j]:
#                     break
#             else:
#                 cnt+=1
#     return cnt



arr=[
    [2,4,1,5,3,2,6],
    [3,5,1,8,7,1,7],
    [8,3,2,7,1,3,8],
    [6,1,2,3,2,1,1],
    [1,3,1,3,5,3,2],
    [1,1,2,5,6,5,2],
    [1,2,2,2,2,1,5]
]
print(solution(arr))