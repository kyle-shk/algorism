li=[]
for _ in range(8):
    a=int(input())
    li.append(a)
y=sorted(li)

z=[]
for i in range(3,len(y)):
    z.append(li.index(y[i]))
r=[1,1,1,1,1]
c=[]
for i in range(len(z)):
    c.append(z[i]+r[i])

print(sum(y[-5:]))
c.sort()
q,w,e,r,t=c
print(q,w,e,r,t)

# https://duwjdtn11.tistory.com/493