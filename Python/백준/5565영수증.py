# n=int(input())
# list=[]
# for _ in range(n):
#     a=int(input())
#     list.append(a)
# print(list)
# sum2=sum(list[1:])
# sum=list[0]-sum2
# print(sum)

t = int(input())
li = [int(input()) for _ in range(9)]
print(t-sum(li))
