# 1. 피연산자는 그대로 출력합니다.
# 2. 연산자는 스택이 비어있으면 자신을 바로 추가합니다.
# 3. stack의 top이 자신보다 우선순위가 낮은 연산자를 만날 때까지 pop 하고 자신을 담습니다.
# 4. 단, 여는 괄호는 닫는 괄호가 아니면 pop하지 않는다.
# 4. 닫는 괄호가 나오면 여는 괄호가 나올 때까지 꺼내서 출력합니다.
# 5. 마지막에 도착하면 스택에서 차례로 꺼내서 출력합니다.
# https://woongsios.tistory.com/288


a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            # ( 안의 부호들은 다빼자
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)



    