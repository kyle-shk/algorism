c=int(input())
a=list(map(int,input().split()))
b=int(input())
count=0
for i in range(len(a)):
    if b == a[i]:
        count+=1
print(count)

