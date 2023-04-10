n = int(input())
factorial = 1
for i in range(1, n+1):
    factorial *= i

cnt = 0
for j in str(factorial)[::-1]:
    if j == '0':
        cnt += 1
    elif j != '0':
        print(cnt)
        break
