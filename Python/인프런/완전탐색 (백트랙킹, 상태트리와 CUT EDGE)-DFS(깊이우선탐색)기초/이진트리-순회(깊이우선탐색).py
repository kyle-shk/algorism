# def DFS(v):
#     if v>7:
#         return
#     else:
#         print(v) #전위순회 방식: 자기일을 먼저하고 다음일을함
#         DFS(v*2)
#         DFS(v*2+1)


# if __name__ == '__main__':
#     DFS(1)

# def DFS(v):
#     if v>7:
#         return
#     else:
#         DFS(v*2)
#         print(v) #중위순회 방식
#         DFS(v*2+1)


# if __name__ == '__main__':
#     DFS(1)

def DFS(v):
    if v>7:
        return
    else:
        DFS(v*2)
        DFS(v*2+1)
        print(v,end=' ') #후위순회 방식


if __name__ == '__main__':
    DFS(1)