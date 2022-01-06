# def lcm(a,b):
#     # a,b = map(int,input().split())
#     A,B=a,b
#     # 작은수는 큰변수로 옮기고 큰수를 작은수로나눈나머지는 작은변수로 옮긴다.
#     # 여기서 작은변수는 b 큰변수는 a
#     while b != 0:
#         a = a%b
#         a,b= b,a
#         # a는 작은변수에서 최대공약수
#     gcd = a
#     lcmm = A * B // gcd
#     return lcmm
# print(lcm(10,15))

m=int(input())

for i in range(m):
    a,b=map(int,input().split())
    A,B=a,b
    while b!=0:
        a = a%b
        a,b = b,a
    gcd = a
    lm = A*B // gcd
    print(lm)

