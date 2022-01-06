m=int(input())
max1 = []
for i in range(m):
    a=list(map(int,input().split()))
    a.sort()
    # print(a)
    if a[0] == a[1] == a[2]:
        max1.append(10000 + a[0] * 1000)
    elif a[0] == a[1] != a[2]:
        max1.append(1000 + a[0] * 100)
    elif a[0] != a[1] == a[2]:
        max1.append(1000 + a[1] * 100)
    elif a[0] != a[1] != a[2]:
        max1.append(a[2] * 100)
   

print(max(max1))
