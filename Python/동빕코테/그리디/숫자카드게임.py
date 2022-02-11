a,b=map(int,input().split())
k=[ list(map(int,input().split())) for _ in range(a)]

li=[]
for i in k:
    e=min(i)
    li.append(e)
print(max(li))