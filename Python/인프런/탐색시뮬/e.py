n,m=list(map(int, input().split()))
a=list(map(int, input().split()))
p1=p2=0
count=0

while p1 !=n and p2!=n:
    if p1 == p2:
        p2+=1
    elif p2>p1:
        if p1 != 0:
            if sum(a[:p1]) == m:
                count+=1
                p1+=1
        else:
            p2+=1
        if p1 == 0:
            if a[p1] == m:
                count+=1
                p1+=1
            else:
                p2+=1
print(count)