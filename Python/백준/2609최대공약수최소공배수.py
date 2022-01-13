import math
a,b=map(int,input().split())
A,B=a,b
while b!=0:
    a,b=b,(a%b)
#     print(a,b)
# print()
b=A*B/a
print(a)
print(math.floor(b))