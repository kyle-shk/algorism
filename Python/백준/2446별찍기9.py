# n=int(input())


# for i in range(n,1,-1):
#     print(' '*(n-i)+'*'*(2*i-1))
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*(2*i-1))

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print('You get {} piece(s) and your dad gets {} piece(s).'.format(a//b,a%b))