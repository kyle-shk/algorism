num = int(input())
sum1=100
sum2=100
for i in range(num):
    a,b = map(int,input().split())
    if a>b:
        sum2 = sum2-a
        # print('sum2 : ',sum2)
    elif a<b:
        sum1 = sum1-b
        # print('sum1 : ',sum1)
    else:
        continue
print(sum1) 
print(sum2) 