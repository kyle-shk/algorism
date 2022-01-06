# x_ = []
# y_ = []
# for i in range(3):
#         x, y = map(int, input().split())
#         x_.append(x)
#         y_.append(y)
# for i in range(3):
#         if x_.count(x_[i]) == 1:
#                 x = x_[i]
#         if y_.count(y_[i]) == 1:
#                 y = y_[i]
# print(x, y)
x1=[]
y1=[]
for i in range(3):
    x,y=map(int,input().split())
    x1.append(x)
    y1.append(y)
for i in range(3):
    if x1.count(x1[i]) == int(1):
        x = x1[i]
    if y1.count(y1[i]) == int(1):
        y = y1[i]
print(x,y)