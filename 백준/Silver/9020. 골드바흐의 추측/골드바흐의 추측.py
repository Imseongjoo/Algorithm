def prime(k):
    if k == 1:
        return 0
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return 0
    return 1

for i in range(int(input())):
    n = int(input())
    for j in range(n//2, 0, -1):
        if prime(j) and prime(n-j):
            print(j, n-j)
            break