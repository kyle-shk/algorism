n = int(input())
cnt = n
for _ in range(n):
    a = input()
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            if a[i+1] in a[:i+1]:
                cnt -= 1
                break
print(cnt)

# https://kbwplace.tistory.com/73
