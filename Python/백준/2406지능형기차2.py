list1=[]
for i in range(10):
    a=list(map(int,input().split()))
    list1.extend(a)


sum1=0
max1=0
for j in range(1,len(list1),2):
    sum1 += list1[j] 
    if max1 < sum1:
        max1 = sum1
    if j+1 >= len(list1):
        break
    sum1 = sum1 - list1[j+1]
print(max1)
    
# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-2460%EB%B2%88-%EC%A7%80%EB%8A%A5%ED%98%95-%EA%B8%B0%EC%B0%A8-2-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython