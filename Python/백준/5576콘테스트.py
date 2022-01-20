li1=[]
li2=[]


for j in range(10):
    a=int(input())
    li1.append(a)
for k in range(10):
    b=int(input())
    li2.append(b)
li1.sort(reverse=True)
li2.sort(reverse=True)
sum1=sum(li1[:3])
sum2=sum(li2[:3])
print(sum1,sum2)
