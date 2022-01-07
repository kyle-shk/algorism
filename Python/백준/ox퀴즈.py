num=int(input())

sum=0
nn = 0
for i in range(num):
    a=list(input())
    # print(a)
    for i in a:
        if i == 'O':
            nn +=1
            sum += nn
        else:
            nn=0
    print(sum)
    sum=0
    nn=0