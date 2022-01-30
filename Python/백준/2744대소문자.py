n=list(map(str,input()))

li=[]
for i in range(len(n)):
    if n[i] == n[i].upper():
        li.append(n[i].lower())
    elif n[i] == n[i].lower():
        li.append(n[i].upper())
print(''.join(li))
