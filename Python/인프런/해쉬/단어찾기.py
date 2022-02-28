n=int(input())
p=dict()

for i in range(n):
    word=input()
    p[word]=1
for j in range(n-1):
    word=input()
    p[word]=0

for a,b in p.items():
    if b == 1:
        print(a)
        break