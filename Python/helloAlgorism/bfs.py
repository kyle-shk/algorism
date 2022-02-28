# 이문제는 가장 짧은경로를 찾는문제

graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob']=['anuj','peggy']
graph['alice']=['peggy']
graph['claire'] = ['thom','jonny']
graph['anuj']=[]
graph['peggy']=[]
graph['thom']=[]
graph['jonny']=[]

from collections import deque
search_queue = deque()
# seach -> deque([])
search_queue += graph['you']
# deque(['alice', 'bob', 'claire'])

def person_is_seller(name):
    return name[-1] == 'y'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft() # 첫번째 사람 꺼냄
        if not person in searched:
            if person_is_seller(person):
                print('{} is a mango seller'.format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
search('you')
