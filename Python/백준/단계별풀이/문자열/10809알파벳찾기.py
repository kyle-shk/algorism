n = input()
ab = 'abcdefghijklmnopqrstuvwxyz'

for i in ab:
    if i in n:
        print(n.index(i), end=' ')
    else:
        print('-1', end=' ')
