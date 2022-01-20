
li=[]
for i in range(5):
    a=list(map(int,input().split()))
    li.append(a)
sum2=0
count=0
for j in range(len(li)):
    if sum(li[j]) > sum2:
        sum2 = sum(li[j])
        count=j
print(count+1,sum2)

# https://heewon9809.tistory.com/255