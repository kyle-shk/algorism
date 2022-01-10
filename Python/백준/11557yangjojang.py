t = int(input())

for i in range(t):
    n = int(input())
    dic = dict()
    for _ in range(n):
        univ, score = map(str, input().split())
        dic[int(score)] = univ
     
    print(dic[max(dic.keys())])


