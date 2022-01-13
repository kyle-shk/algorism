n=int(input())

# 면의수=2-꼭-모
# a=꼭,b=모
# 2-a-b

for _ in range(n):
    a,b=map(int,input().split())
    m=2-a+b
    print(m)