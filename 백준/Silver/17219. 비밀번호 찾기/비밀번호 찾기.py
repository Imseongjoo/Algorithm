n, m = map(int, input().split())

password = {}
for i in range(n):
    site, pw = input().split()
    password[site] = pw

for i in range(m):
    site = input()
    print(password[site])