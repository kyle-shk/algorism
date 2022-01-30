a,b=map(str,input().split())

def Rev(n):
    return n[::-1]
print(int(Rev(str(int(Rev(a))+int(Rev(b))))))