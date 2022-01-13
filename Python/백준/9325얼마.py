n=int(input())

for i in range(n):
    a=int(input())
    num=int(input())
    sum=0
    for i in range(num):
        b,c=map(int,input().split())
        if b==0 or c==0:
            break
        sum += b*c
    total=sum+a
    print(total)