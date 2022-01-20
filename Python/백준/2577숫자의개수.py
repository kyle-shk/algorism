sum1=1
for _ in range(3):
    a=int(input())
    sum1 *= a
li = []

for _ in range(10):
    li.append(0)
for i in range(10):
    y=str(sum1).count(str(i))
    li[i] += y
for k in range(len(li)):
    print(li[k])
