a=list(map(str,input().split()))
list=[]
list.append(a[0][::-1])
list.append(a[1][::-1])
print(list)
if int(list[0]) <int(list[1]):
    print(int(list[1]))
else:
    print(int(list[0]))