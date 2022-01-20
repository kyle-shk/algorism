li=[]
for _ in range(10):
    a=int(input())
    li.append(a)

y=list(set(li))
z=[]
for i in range(len(y)):
    z.append(li.count(y[i]))
# print(z)
        
print(sum(li)//len(li))
print(y[z.index(max(z))])


# https://thingjin.tistory.com/entry/%EB%B0%B1%EC%A4%80-2592%EB%B2%88-%EB%8C%80%ED%91%9C%EA%B0%92-%ED%8C%8C%EC%9D%B4%EC%8D%AC