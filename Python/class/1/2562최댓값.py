m = 0
t = 0
for i in range(9):
    n = int(input())
    if m < n:
        m = n
        t = i
print(m)
print(t+1)
