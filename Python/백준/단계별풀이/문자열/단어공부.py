n = input()
n = n.lower()
a = set(n)
li = []
for i in a:
    li.append(n.count(i))

if li.count(max(li)) >= 2:
    print('?')
else:
    print(list(a)[li.index(max(li))].upper())
