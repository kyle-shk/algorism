def solution(s):
    answer = True
    s=s.lower()
    pC=0
    yC=0
    for i in s:
        if i == 'p':
            pC+=1
        elif i == 'y':
            yC +=1

    if pC==0 and yC==0:
        return answer
    if pC == yC:
        return answer
    else:
        answer = False
        return answer

  
print(solution('pPoooyY'))


# def numPY(s):
#     # 함수를 완성하세요
#     return s.lower().count('p') == s.lower().count('y')

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( numPY("pPoooyY") )
# print( numPY("Pyy") )