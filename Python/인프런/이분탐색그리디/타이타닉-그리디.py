# a,b=map(int,input().split())
# k=list(map(int,input().split()))
# k.sort()
# cnt=0

# while k:
#     if len(k)==1:
#         cnt+=1
#         break
#     if k[0]+k[-1] > b:
#         k.pop()
#         cnt+=1
#     else:
#         k.pop(0)
#         k.pop()
#         cnt+=1
# print(cnt)

a,b=map(int,input().split())
k=list(map(int,input().split()))
k.sort()
cnt=0

while k:
    if len(k)==1:
        cnt+=1
        break
    if k[0]+k[-1] > b:
        k.pop()
        cnt+=1
    else:
        k.pop(0)
        k.pop()
        cnt+=1
print(cnt)