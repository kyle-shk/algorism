
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    a1=a[0]
    a2=a[1:]
    print('Class {}'.format(i+1))
    a2.sort(reverse=True)
    m1=0
    for j in range(len(a2)-1):
        M=a2[j]-a2[j+1]
        if M> m1:
            m1 = M
    print('Max {}, Min {}, Largest gap {}'.format(max(a2),min(a2),(m1)))