N = int(input())

if N == 0 :
    print(1)
else :
    cnt = 1
    for i in range(2, N+1) :
        cnt *= i
    print(cnt)