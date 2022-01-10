str_list = ['좋은하루','good_morning','굿모닝','niceday']
print(sorted(str_list, key=len))  # 함수
# ['굿모닝', '좋은하루', 'niceday', 'good_morning']

print(sorted(str_list, key=lambda x : x[1]))  # 람다
# ['niceday', 'good_morning', '굿모닝', '좋은하루']
