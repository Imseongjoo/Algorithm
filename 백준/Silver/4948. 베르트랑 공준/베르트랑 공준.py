import sys
def prime(n):
    cnt = 0
    for i in range(n+1, 2*n):
        cnt += 1
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                cnt -= 1
                break
    return cnt

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        print(prime(n))