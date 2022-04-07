# n=int(input())
# a=list(map(int, input().split()))
# a.sort(reverse=True)
# cnt=0
# while len(a) != 0:
#     ar=a[0]
#     del a[0:ar]
#     cnt+=1
# print(cnt)


n = int(input())
array = sorted(list(map(int, input().split())))


result = 0
party = 0
for i in array:
    party += 1
    if party >= i:
        party = 0
        result += 1

print(result)
