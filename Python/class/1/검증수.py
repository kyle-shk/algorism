n = list(map(int, input().split()))
t = 0
for i in n:
    i = i*i
    t += i
    # print(t)
print(t % 10)
