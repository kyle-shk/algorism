# 두번이상 나온이름찾기
# 입력:이름이 n개 들어있는리스트
# 출력:이름 n개중 반복되는 이름의 집합
def find_same_name(a):
    result = []
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                result.append(a[i])
    return result


name=['tom','jerry','mike','tom']
print(find_same_name(name))