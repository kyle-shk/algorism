l = []
for _ in range(10):
    n = int(input())
    n = n % 42
    l.append(n)
l = set(l)
print(len(l))
