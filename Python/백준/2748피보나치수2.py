n=int(input())
list=[]
# 피보나치수열은 0부터시작하므로 전체길이는 +1해줘야함
for _ in range(n+1):
    list.append(0)
# print(list)
list[1]=1

for i in range(2,n+1):
    list[i] = list[i-2] + list[i-1]
# print(list)
print(list[-1])
# https://devjin-blog.com/boj-2748-fib2/