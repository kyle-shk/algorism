
# def Count(capacity):
#     cnt=1
#     sum=0
#     for x in Music:
#         if sum+x>capacity:
#             cnt+=1
#             sum=x
#         else:
#             sum+=x
#     return cnt

# n, m=map(int, input().split())
# Music=list(map(int, input().split()))
# maxx=max(Music)
# lt=1
# rt=sum(Music)
# res=0
# while lt<=rt:
#     mid=(lt+rt)//2
#     if mid>=maxx and Count(mid)<=m:
#         res=mid
#         rt=mid-1
#     else:
#         lt=mid+1
# print(res)


def CountNum(mid):
    sum=0
    cnt=1
    for i in range(len(a)):
        if sum + a[i] >mid:
            cnt+=1
            sum=a[i]
        else:
            sum+=a[i]
    return cnt


n,k=map(int,input().split())

a=list(map(int,input().split()))
a.sort()
start=a[0]
end=sum(a)
max1=max(a)
res=0
while start<=end:
    mid = (start+end)//2
    # dvd하나의 용량이최소 제일큰길이보다는 커야함
    if CountNum(mid) <= k and mid>=max1:
        res=mid
        end=mid-1
    else:
        start=mid+1
print(res)