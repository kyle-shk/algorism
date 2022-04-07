n = input()

sum = ''
for i in n:
    sum += i
    if len(sum) == 10:
        print(sum)
        sum = ''
print(sum)
