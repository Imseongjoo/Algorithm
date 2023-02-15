import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    age,name = map(str, input().split())
    a.append([int(age),name])
b = sorted(a, key=lambda x:x[0])
for j in b:
    print(*j)