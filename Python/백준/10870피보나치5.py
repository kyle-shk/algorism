n=int(input())
li=[]
li.append(0)
li.append(1)
# print(li)
for i in range(2,n+1):
    li.append(li[i-2] +li[i-1])
    # li.append(li[i])
print(li[n])

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# n = int(input())
# print(fibonacci(n))

# https://ooyoung.tistory.com/115