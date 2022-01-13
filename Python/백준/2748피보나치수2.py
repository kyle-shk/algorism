n=int(input())
list=[]
for _ in range(n+1):
    list.append(0)
list[1]=1

for i in range(2,n+1):
    list[i] = list[i-2] + list[i-1]
print(list[-1])
# https://devjin-blog.com/boj-2748-fib2/