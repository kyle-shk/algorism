n=int(input())
a=list(map(int, input().split()))
a.sort()

target=1
for x in a:
    # 만들수없는 금액을 찾으면 반복종료
    if target<x:
        break
    target += x

print(target)
