# def Count(len):
#     cnt=0
#     for x in Line:
#         cnt+=(x//len)
#     return cnt

# k, n=map(int, input().split())
# Line=[]
# res=0
# # largest=0
# for i in range(k):
#     tmp=int(input())
#     Line.append(tmp)
#     # largest=max(largest, tmp)
#     largest=max(Line)

# lt=1
# rt=largest
# while lt<=rt:
#     mid=(lt+rt)//2
#     if Count(mid)>=n:
#         res=mid
#         lt=mid+1
#     else:
#         rt=mid-1
# print(res)

# def checkNumber(mid):
#     cnt=0
#     for num in li:
#         count=num // mid
#         cnt+=count
#     return cnt
# n,k=map(int,input().split())
# li=[]
# res=0
# for _ in range(n):
#     a=int(input())
#     li.append(a)
# li.sort()
# start=1
# end = li[-1]


# while start<=end:
#     mid = (start+end)//2
#     if checkNumber(mid) >= k:
#         res=mid
#         start=mid+1
#     else:
#         end=mid-1
# print(res)



a,b=map(int, input().split())
line=[]
for _ in range(a):
    c=int(input())
    line.append(c)
    largest = max(line)
lt=1
rt=largest
res=0
count=0
while lt<=rt:
    mid = (lt+rt) //2
    for d in line:
        count += d // mid
    if count >= b:
        res=mid
        lt= mid+1
        count=0
    elif count <=b:
        rt=mid-1
        count=0
print(res)