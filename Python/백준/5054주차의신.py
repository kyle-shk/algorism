n=int(input())

for _ in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    b.sort()
    c=(b[-1]-b[0])*2
    print(c)