n=int(input())
li=[]
for _ in range(n):
    a,b=map(int,input().split())
    li.append((a,b))

li.sort(reverse=True)
cnt=0
largest=0
answer=[]
for a,b in li:
    if b>largest:
        largest=b
        answer.append((a,b))
        cnt+=1
print(cnt)
print(answer)