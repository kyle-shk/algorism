T=int(input())

for i in range(T):
    n=int(input())
    total_credit=0
    total_grade=0
    for i in range(n):
        a,b=map(float,input().split())
        total_credit += a
        total_grade += a * b
    gpa = total_grade / total_credit
    print(int(total_credit),round(gpa,1))

    # https://claude-u.tistory.com/358