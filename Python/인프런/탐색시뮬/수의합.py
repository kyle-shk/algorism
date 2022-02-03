n,m=map(int,input().split())
a=list(map(int,input().split()))
lt=0
rl=1
cnt=0
tot=a[0]
while True:
    if tot<m:
        if rl<n:
            tot += a[rl]
            rl+=1
        else:
            break
    elif tot ==m:
        cnt+=1
        tot -= a[lt]
        lt+=1
    else:
        tot -= a[lt]
        lt+=1
print(cnt)
        