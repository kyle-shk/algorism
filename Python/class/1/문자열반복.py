n = int(input())
for _ in range(n):
    t = ''
    a, b = map(str, input().split())
    for i in b:
        t += int(a)*i
    print(t)
