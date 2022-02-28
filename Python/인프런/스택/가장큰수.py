def solution(a,b):
    num=list(map(int,str(a))) #숫자화
    print(num)
    stack=[]
    for x in num:
        while stack and b>0 and stack[-1] <x:
            stack.pop()
            b-=1
        stack.append(x)
    if b !=0:
        stack = stack[:-b]
    return ''.join(map(str,stack))

num=9977252641
m=5
print(solution(num,m))

# stack만듬
# 1.전체배열중 맨앞에있는수를고름
# 그수와 stack의 마지막에있는수와비교 -> stack의수가작다? -> 꺼냄 -> 1반복
#                             -> stack의수가크다? -> 그수 stack에넣음
# 만일 stack이랑비굔느다했는데 m이남았다
# 전체스택중 m보다앞부분만 짤라서 return