def Insertion_Sort(array):
    for a in range(1, len(array)):
        for b in range(a, 0, -1):
            if array[b] < array[b-1]:
                   array[b], array[b-1] = array[b-1], array[b]
            else:
                   break
    return array
d=[2,4,5,1,3]
Insertion_Sort(d)
print(d)

