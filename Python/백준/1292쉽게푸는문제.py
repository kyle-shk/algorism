x, y = map(int, input().split())
a = []
for i in range(1,50):
    a.extend([i] * i)
print(sum(a[x-1:y]))