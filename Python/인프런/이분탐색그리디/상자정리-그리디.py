n=int(input())
li=list(map(int,input().split()))
k=int(input())
li.sort(reverse=True)

cnt=0
while cnt !=k:
    cnt+=1
    max1=li.pop(0)
    min1=li.pop()
    li.insert(0,max1-1)
    li.append(min1+1)
    li.sort(reverse=True)

print(li[0]-li[-1])

# n=int(input())
# li=list(map(int,input().split()))
# k=int(input())
# li.sort(reverse=True)

# li.sort()
# for _ in range(k):
#     li[0]+=1
#     li[n-1]-=1
#     li.sort()
# print(li[n-1]-li[0])