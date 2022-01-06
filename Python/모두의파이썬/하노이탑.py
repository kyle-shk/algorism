# 하노이탑
# 입력:옮기려는 원반의 개수:n
    # 옮길 원반이 현재있는 출발점 기둥:from_pos
    # 원반을 옮길 도착점 기둥:to_pos
    # 옮기는 과정에서 사용할 보조기둥:aux_pos
# 출력:원반을 옮기는 순사

def hanoi(n,from_pos,to_pos,aux_pos):
    if n==1:
        print(from_pos,'->',to_pos)
        return
    # 원반 n-1개를 aux_pos로 이동(to_pos는 보조기둥)
    hanoi(n-1,from_pos,aux_pos,to_pos)
    # 가장큰 원반은 도착점으로
    print(from_pos,'->',to_pos)
    # aux_pos에있는 원반n-1개를 목적지로 이동(from_pos는 보조기둥)
    hanoi(n-1,aux_pos,to_pos,from_pos)
print('n=2')
print(hanoi(3,1,3,2))