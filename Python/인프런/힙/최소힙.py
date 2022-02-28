import heapq as hq

a=[]
while True:
    n=int(input())
    if n== -1:
        break
    if n==0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a,n)

# heap 개념정리
# 최솟값구하는법
# 1.부모노드는 자식노드보다 크면안됨
# 2.하나씩 푸시할때 만약 부모노드가 자식노드보다 크면 자식중에서 가장작은애랑 바꾸는식으로 전개
# 3.만약 부모노드가 pop되서 빠져나가면 빈자리는 오른쪽 끝에있는애가 채우면 위의 과정 반복