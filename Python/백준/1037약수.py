# n=int(input())


# a=list(map(int,input().split()))

# a.sort()
# if len(a) == 1:
#     print(a[0] *2)
# if len(a) == 2:
#     print(a[1] *2)
# li=[]
# # print('a',a)
# if len(a) >= 3:
#     li=a[-2:]
#     # print('li',li)
#     while li[1] !=0:
#         A,B=li[0],li[1]
#         li[0],li[1]=li[1],int(li[1]/li[0])
#         lcd=int(A*B/li[0])
#     print(lcd*2)

n = int(input())
a = list(map(int, input().split()))
a_max = max(a)
a_min = min(a)
print(a_max * a_min)
