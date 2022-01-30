
a=list(map(str,input()))
while len(a) > 0:
    num=a[:10]
    print(''.join(num))
    a=a[len(num):]
