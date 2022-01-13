
# N = int(input())

# for i in range(N,0,-1):

#     b = ' '*(N-i)+'*'*((2*i)-1)

#     print(b)

N=int(input())
for i in range(1,N+1):
    print(" "*(N-i)+"*"*(2*i-1))
for k in range(N-1,0,-1):
    print(" "*(N-k)+"*"*(2*k-1))