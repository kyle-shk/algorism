def solution(s):
    answer = ''
    # answer += ''.join(sorted(s)[::-1])
    a=sorted(list(s),reverse=True)
    answer += ''.join(a)
    
    return answer
print(solution('Zbcdefg'))

# https://kkkkhd.tistory.com/493
