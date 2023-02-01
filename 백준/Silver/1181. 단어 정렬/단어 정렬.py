import sys

n = int(sys.stdin.readline())
ls = []

for i in range(n):
    ls.append(sys.stdin.readline().strip())
set_ls = set(ls)
ls = list(set_ls)
ls.sort()
ls.sort(key = len)

for i in ls:
    print(i)