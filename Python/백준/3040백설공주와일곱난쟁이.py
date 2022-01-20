li=[]
for i in range(9):
    a=int(input())
    li.append(a)
li.sort(reverse=True)
for i in range(0,len(li)-1):
    for j in range(i+1,len(li)):
        li1 = li[i] + li[j]
        if sum(li) - li1 == 100:
            li.pop(j)
            li.pop(i)
            break
li.sort()
for k in li:
    print(k)