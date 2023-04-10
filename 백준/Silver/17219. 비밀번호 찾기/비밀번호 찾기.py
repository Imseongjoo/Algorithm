import sys

n, m = map(int, input().split())

password = {}
for i in range(n):
    site, pw = sys.stdin.readline().split()
    password[site] = pw

for i in range(m):
    site = sys.stdin.readline().rstrip()
    print(password[site])