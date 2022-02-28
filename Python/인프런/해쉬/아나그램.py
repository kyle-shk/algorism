p1={}
p2={}
a=input()
b=input()

for i in range(len(a)):
    p1[i] = p1.get(i,0)+1
for i in range(len(a)):
    p2[i] = p2.get(i,0)+1


for i in p1.keys():
    if i in p2.keys():
        if p1[i] != p2[i]:
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES')

# 개선된 코드
# a=input()
# b=input()
# sH=dict()

# for i in a:
#     sH[i] = sH.get(i,0)+1
# for i in b:
#     sH[i] = sH.get(i,0)-1

# for x in a:
#     if sH.get(x) > 0:
#         print('NO')
#         break
# else:
#     print('YES')