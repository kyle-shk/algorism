# T = int(input())

# for _ in range(T):
#     num = int(input())
#     dic={}
#     for i in range(num):
#         a,b=map(str,input().split())
#         dic[int(a)]=b
#     # print(dic)
#     print(dic[max(dic.keys())])

n=int(input())
for i in range(1,10):
    print('{} * {} = {}'.format(n,i,n*i))