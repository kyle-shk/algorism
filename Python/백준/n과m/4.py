n,m=list(map(int,input().split()))
# a=list(map(int,input().split()))
# a.sort()

s=[]
def D(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in range(start,n+1):
        # if i not in s:
            s.append(i)
            D(start+1)
            s.pop()

D(1)