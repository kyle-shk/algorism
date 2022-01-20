n=int(input())

for _ in range(n):
    a,b=map(int,input().split())
    li=[]
    for i in range(a):
        c=int(input())
        li.append(c)
    li.sort(reverse=True)
    for j in range(b):
        if (j+1) in li:
            li.pop()
    print(len(li))