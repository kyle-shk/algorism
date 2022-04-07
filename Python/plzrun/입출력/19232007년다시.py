# Day = 0
# arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

# x, y = map(int, input().split())

# for i in range(x-1):
#     Day = Day + arrList[i]
# Day = (Day + y) % 7

# print(weekList[Day])

week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
sum = 0  # 날(day)의 총 합
a = [1, 3, 5, 7, 8, 10, 12]  # 31일인 달
b = [4, 6, 9, 11]  # 30일인 달

m, d = map(int, input().split())

for i in range(1, m):  # 1월인 경우는
    if i in a:
        sum += 31
    elif i in b:
        sum += 30
    elif i == 2:
        sum += 28  # 2월은 28일까지

sum += d
print(week[sum % 7])
