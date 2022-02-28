# 연산자아님? -> stack넣음
#  연산자? -> 인덱스 -1,인덱스-2꺼내서 연산자랑계산후 -> 다시 stack에넣음
a=input()
stack=[]
temp=[]
sum=0

for i in a:
    if i.isdigit():
        i=int(i)
        stack.append(i)
    else:
        # if i.isalpha():
        if i == '+':
            while stack and len(temp) != 2:
                temp.append(stack.pop())
            temp.sort(reverse=True)
            sum += int(temp[0])+int(temp[1])
            stack.append(sum)
            sum=0
            temp.clear()
        elif i == '-':
            while stack and len(temp) != 2:
                temp.append(stack.pop())
            temp.sort(reverse=True)
            sum += int(temp[0])-int(temp[1])
            stack.append(sum)
            sum=0
            temp.clear()
        elif i == '*':
            while stack and len(temp) != 2:
                temp.append(stack.pop())
            temp.sort(reverse=True)
            sum += int(temp[0])*int(temp[1])
            stack.append(sum)
            sum=0
            temp.clear()
        elif i == '/':
            while stack and len(temp) != 2:
                temp.append(stack.pop())
            temp.sort(reverse=True)
            sum += int(temp[0])/int(temp[1])
            stack.append(sum)
            sum=0
            temp.clear()
print(stack[0])

# 강사풀이
# a=input()
# stack=[]
# for x in a:
#     if x.isdecimal():
#         stack.append(int(x))
#     else:
#         if x=='+':
#             n1=stack.pop()
#             n2=stack.pop()
#             stack.append(n2+n1)
#         elif x=='-':
#             n1=stack.pop()
#             n2=stack.pop()
#             stack.append(n2-n1)
#         elif x=='*':
#             n1=stack.pop()
#             n2=stack.pop()
#             stack.append(n2*n1)
#         elif x=='/':
#             n1=stack.pop()
#             n2=stack.pop()
#             stack.append(n2/n1)
# print(stack[0])
