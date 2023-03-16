n, k = map(int, input().split())
a = list(range(1, n+1))
b = []
i = 0
while a:
    i = (i + k - 1) % len(a)
    b.append(str(a.pop(i)))
print("<" + ", ".join(b) + ">")