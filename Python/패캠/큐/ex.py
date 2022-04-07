# 일반적인 queue
# import queue

# data = queue.Queue()
# data.put('12')
# data.put('3')
# print(data)
# print(data.qsize())
# print(data.get())
# print(data.qsize())

# LifoQueue()로 큐 만들기 (LIFO(Last-In, First-Out))
import queue
data_queue = queue.LifoQueue()
