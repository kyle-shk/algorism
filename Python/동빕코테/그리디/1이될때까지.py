a,b=map(int,input().split())
c=0
while a != 1:
    if a%b != 0:
        a= a-1
        c+=1
    else:
        a=a//b
        c+=1
print(c)