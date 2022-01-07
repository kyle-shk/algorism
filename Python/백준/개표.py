# 2개의 입력을 만듬
# 변수 2개를 만듬
# 변수1에는 a일때 +1 변수2는 b일때 +1
a=int(input())
b=list(map(str,input()))
sum1=0
sum2=0
for i in range(a):
    if b[i] == 'A':
        sum1+=1
    else:
        sum2+=1

if sum1 > sum2:
    print('A')
elif sum1 < sum2:
    print('B')
else:
    print('Tie')