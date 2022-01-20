a,b=map(int,input().split())
list=[]

for i in range(1,a+1):
    if a%i==0:
        list.append(i)
# print(list)
if len(list) >= b:
    print(list[b-1])
else:
    print(0)
# print(list)  