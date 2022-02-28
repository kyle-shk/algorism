# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1,len(numbers)):
#             if numbers[i]+numbers[j] not in answer:
#                 answer.append(numbers[i]+numbers[j])
#     return sorted(list(set(answer)))



# a=[2,1,3,4,1]

# print(solution(a))

def solution(arr):
    answer = []
    tmp=9999
    for i in arr:
        if tmp != i:
            answer.append(i)
            tmp = i
        else:
            continue
    return answer

arr = [0,3,1,2,2,3]
print(solution(arr))


# https://jokerldg.github.io/algorithm/2021/04/03/no-same-number.html
# def solution(arr):
#     answer = []
#     answer.append(arr[0])
    
#     for i in range(1, len(arr)):  
#         if arr[i-1] != arr[i]:
#           answer.append(arr[i])

#     return answer