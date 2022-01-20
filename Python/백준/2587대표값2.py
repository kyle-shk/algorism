li=[]
for i in range(5):
    a=int(input())
    li.append(a)
li.sort()
print(sum(li)//len(li))
print(li[2])