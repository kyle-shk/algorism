n=int(input())
li=[]
for i in range(n):
    a=int(input())
    if a == 0:
        li.pop()
    else:
        li.append(a)
    
   
print(sum(li))

# https://itprogramming119.tistory.com/entry/%EB%B0%B1%EC%A4%80%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-10773%EB%B2%88-%EC%A0%9C%EB%A1%9C-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython