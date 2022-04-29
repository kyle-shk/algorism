# 3중 for문
# n,m=map(int, input().split())

# a=list(map(int,input().split()))

# w=0
# for i in range(n-2):
#     for j in range(i+1,n-1):
#         for k in range(j+1,n):
#             if a[i]+a[j]+a[k] == m:
#                 w=a[i]+a[j]+a[k]
#                 # print(w)
#                 break
#             elif a[i]+a[j]+a[k] > m:
#                 continue
#             else:
#                 if w < a[i]+a[j]+a[k]:
#                     w = a[i]+a[j]+a[k]

                                  
# print(w)

# n, m = map(int, input().split())
# num = list(map(int, input().split()))
# l = len(num)
# ans = 0
# for i in range(0, l-2):
#     for j in range(i+1, l-1):
#         for k in range(j+1, l):
#             if(num[i] + num[j] + num[k] > m):
#                 continue
#             else:
#                 ans = max(ans ,num[i] + num[j] + num[k])

# print(ans)

from itertools import permutations

n, m = map(int, input().split())

num = list(map(int, input().split()))
permutationArray = permutations(num, 3)
# print('p',permutationArray)
ans = 0
for i in permutationArray:
    print('i',i)
    if(m+1 > sum(i)):
        ans = max(ans, sum(i))
    
print(ans)

# https://velog.io/@jeongdopark/Algorithm-python-%EB%B0%B1%EC%A4%80-2798%EB%B2%88
# https://duwjdtn11.tistory.com/297