n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()

s=[]
def D(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in range(start,n):
            s.append(a[i])
            D(i)
            s.pop()
     
D(0)

