a=input()
cnt=[0]*26

for i in a:
    cnt[ord(i)-97]+=1
print(*cnt)