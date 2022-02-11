# 어려워....
# def Count(len):
#     cnt=1
#     ep=Line[0]
#     for i in range(1, n):
#         if Line[i]-ep>=len:
#             cnt+=1
#             ep=Line[i]
#     return cnt

# n, c=map(int, input().split())
# Line=[]
# for _ in range(n):
#     tmp=int(input())
#     Line.append(tmp)
# Line.sort()
# # lt는 최소거리길이 rt는 최대거리길이
# lt=1
# rt=Line[n-1]
# while lt<=rt:
#     mid=(lt+rt)//2
#     if Count(mid)>=c:
#         res=mid
#         lt=mid+1
#     else:
#         rt=mid-1

# print(res)

def CountNum(mid):
    cnt=1
    ep=li[0]
    for num in range(1,len(li)):
        if li[num]-ep>=mid:
            cnt+=1
            ep=li[num]
    return cnt


n,k=map(int,input().split())
li=[]
for _ in range(n):
    a=int(input())
    li.append(a)
li.sort()
start=1
end=li[-1]
res=0
while start<=end:
    mid = (start+end)//2
    if CountNum(mid)>=k:
        res=mid
        start=mid+1
    else:
        end=mid-1
print(res)