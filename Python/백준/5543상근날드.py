li=[]

for i in range(5):
    a=int(input())
    li.append(a)
ham=min(li[0:3])
cok=min(li[3:])
print(ham+cok-50)