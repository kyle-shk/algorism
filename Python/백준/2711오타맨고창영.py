n=int(input())

for _ in range(n):
    a,b=input().split();
    if a==1:
        b=b[1:]
    else:
        b=b[0:int(a)-1]+b[int(a):]  #b[int(a)-1:int(a)]
    print(b)
