# 연속한 숫자의 곱을 구하는 알고리즘
# 입력:n
# 출력:1부터 n까지 연속한 숫자의합

def func(n):
    f=1
    for i in range(1,n+1):
        f *= i
    return f
print(func(10))