def stack(start , end):
    if start <= end:
        print('Push :', start)
        stack(start + 1, end)
        print("Pop  :", start)
    else:
        print("--------")

stack(0, 5)