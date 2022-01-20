a,b=map(int,input().split())

li=[]
for i in range(a):
    c=int(input())
    li.append(c)
li.sort(reverse=True)
li2=[]
for k in range(len(li)):
    if li[k] > b:
        break
    else:
        if sum(li2) > b:
            li2.pop()
        while sum(li2) < b:
            li2.append(li[k])
print(len(li2))