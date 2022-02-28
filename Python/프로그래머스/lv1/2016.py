def solution(a, b):
    answer = ''
    date =["THU","FRI","SAT","SUN","MON","TUE","WED"] #['MON','TUE','WED','THU','FRI','SAT','SUN']
    num=[31,29,31,30,31,30,31,31,30,31,30,31]
    answer+=date[(sum(num[:a-1])+b)%7]
    return answer
print(solution(1,1))

# https://sinsomi.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Python-2016%EB%85%84-%EC%B4%88%EC%BD%94%EB%8D%94