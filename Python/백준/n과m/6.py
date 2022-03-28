n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()

s=[]
def D(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
    for i in range(start,n):
        if a[i] not in s:
            s.append(a[i])
            D(i+1)
            s.pop()
     
D(0)