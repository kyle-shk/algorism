n=int(input())
a=[list(map(int,input().split())) for _ in range(n)] # 2중배열만들기
m=int(input())

# 배열을 회전하는방법
# 1.어느장향으로회전할건지정함
# 2.왼쪽이면->앞에있는걸빼서 뒤로넘기는식으로회전, 오른쪽이면->뒤쪽에있는걸빼서 맨앞에넣어줌
for i in range(m):
    q,w,e=map(int,input().split())
    if w ==0:
        for _ in range(e):
            a[q-1].append(a[q-1].pop(0))
    else:
        for _ in range(e):
            a[q-1].insert(0,a[q-1].pop())
# 모래시계모양으로 더하기
res=0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res += a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)


