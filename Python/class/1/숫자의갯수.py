t = 1
for _ in range(3):
    n = int(input())
    t *= n
print(t)
l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in str(t):
    if l[int(i)] > 0:
        l[int(int(i))] += 1
    else:
        l[int(int(i))] = 1
    print(l)
for i in l:
    print(i)

# https://wook-2124.tistory.com/233
