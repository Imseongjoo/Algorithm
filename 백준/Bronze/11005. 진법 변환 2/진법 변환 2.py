from sys import stdin

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, stdin.readline().split())
answer = ''

while n != 0:
    answer += str(tmp[n % b])
    n = n // b

print(answer[::-1])