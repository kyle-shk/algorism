# 리스트 형태로 입력받음
# 반복횟수를 입력받음
# 2번쨰원소와 3번쨰원소의 차를 첫번쨰원소와 비교했을떄 결과물에따른 값을 조건문으로 표현
num=int(input())
for i in range(num):
    a=list(map(int,input().split()))
    print(a)
    if a[1]-a[2] > a[0]:
        print('advertise')
    elif a[1]-a[2]==a[0]:
        print('does not matter')
    else:
        print('do not advertise')