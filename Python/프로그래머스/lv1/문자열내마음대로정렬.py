def solution(strings, n):
    
    strings.sort(key=lambda x: (x[n],x))
    return strings

arr=["abcd", "abce", "cdx"]
print(solution(arr,1))

# https://codingpractices.tistory.com/57