n=int(input())

for k in range(n):
    a=input().lower()
    answer = 'YES'
    for i in range(round(len(a)/2)):
        if a[i] == a[len(a)-i-1]:
            if i == round(len(a)/2)-1:
                print('{} {}'.format(k+1,answer))
            else:
                continue
        else:
            answer = 'NO'
            print('{} {}'.format(k+1,answer))
            break
# n=int(input())
# for i in range(n):
#     str=input()
#     str=str.upper()
#     if str==str[::-1]:
#         print("#%d YES" %i)
#     else:
#         print("#%d NO" %i)