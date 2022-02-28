def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    # print(set_reserve)
    set_lost = set(lost)-set(reserve)
    # print(set_lost)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)
lost=[2,4]
reserve=[2,4,5]

print(solution(5,lost,reserve))

# https://rain-bow.tistory.com/30