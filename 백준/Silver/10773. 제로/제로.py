k = int(input())
ls = []
for i in range(k):
    n = int(input())
    if n == 0:
        ls.pop()
    else:
        ls.append(n)
print(sum(ls))