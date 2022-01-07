num = int(input())

sum1=0
sum2=0

for i in range(num):
    m=int(input())
    if m == 1:
        sum1 +=1
    elif m ==0:
        sum2 +=1
if sum1 > sum2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")