def minn(a):
    mon_idx=0
    n=len(a)
    for i in range(1,n):
        if a[mon_idx] > a[i]:
            mon_idx = i
    return mon_idx


a=[127,92,18,33,58,33,42]
print(minn(a))