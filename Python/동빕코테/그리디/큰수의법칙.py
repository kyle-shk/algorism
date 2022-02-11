# 내답
# a,b,c=map(int,input().split())
# l=list(map(int,input().split()))
# cnt=0
# sum1=0
# count=0
# l.sort(reverse=True)
# while cnt != b:
#     if count != c:
#         cnt+=1
#         count+=1
#         sum1 += l[0]
#     else:
#         cnt+=1
#         count=0
#         sum1 += l[1]
# print(sum1)
        
# 단순하게 푸는 답안제시
n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
first = data[n-1] # 가장큰수
second = data[n-2] # 두번째롯큰수

result = 0

while True:
    for i in range(k): # 가장큰수를 k번 더하기
        if m ==0:
            break
        result += first
        m-=1 #더할때마다 1씩빼기
    if m==0:
        break
    result == second
    m-=1
print(result)