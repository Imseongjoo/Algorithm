N = int(input())
for i in range(N):
    a = input()
    c = list(a)
    sum = 0
    cnt = 1
    for j in c:
        if j == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)    