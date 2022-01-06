# 리스트에서 최솟값의 위치를 돌려주는 함수

# def find_min_idx(a):
#     min_idx=0
#     for i in range(len(a)):
#         if a[i]<a[min_idx]:
#             min_idx = i
#     return min_idx

# def sel_sort(a):
#     result = []
#     while a:
#         min_idx = find_min_idx(a)
#         value = a.pop(min_idx)
#         result.append(value)
#     return result



# d=[2,4,5,1,3]
# print(sel_sort(d))

# pop함수는 pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다.

# >>> a = [1,2,3]
# >>> a.pop(1)
# 2
# https://wikidocs.net/14#pop

# array.append(x) 형태로 사용한다. 

# append는 덧붙인다는 뜻으로 괄호( ) 안에 값을 입력하면 새로운 요소를 array 맨 끝에 객체로 추가한다. 요소를 추가할 때는 객체로 추가하게 되는데, 입력한 값이 리스트와 같은 반복 가능한 iterable 자료형이더라도 객체로 저장한다. 사용 예시는 아래와 같다.

# >>> nums = [1, 2, 3]
# >>> nums.append(4)
# [1, 2, 3, 4]

# >>> nums.append([5, 6])
# [1, 2, 3, 4, [5, 6]] # 리스트가 하나의 객체로 추가되었음

# https://ooyoung.tistory.com/117

# 일반적인 풀이

def sel_sort(a):
    for i in range(0,len(a)-1):
        min_idx = i
        for j in range(i+1,len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx],a[i]


d=[2,4,5,1,3]
sel_sort(d)
print(d)