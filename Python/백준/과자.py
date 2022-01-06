a,b,c=map(int,input().split())

d=a*b
if d == c:
    print('0')
elif d>c:
    print(d-c)
elif d<c:
    print('0')