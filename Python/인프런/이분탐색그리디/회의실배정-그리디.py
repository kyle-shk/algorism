n=int(input())
li=[]
# 튜플함수 리스트안에 넣기
for _ in range(n):
    a,b=map(int,input().split())
    li.append((a,b))
# 튜플기준 오른쪽값을 기준으로 오름차순으로 정렬
li.sort(key=lambda x: x[1])

et=0
cnt=0
for x,y in li:
    if x>=et:
        et=y
        cnt+=1
print(cnt)

# sort+lambda정렬 https://gorokke.tistory.com/38, https://dailyheumsi.tistory.com/67
# 람다개념: https://dojang.io/mod/page/view.php?id=2359