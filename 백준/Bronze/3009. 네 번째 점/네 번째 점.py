a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
g = 0
h = 0

if a == c:
    g += e
elif c == e:
    g += a
elif a == e:
    g += c

if b == d:
    h += f
elif d == f:
    h += b
elif b == f:
    h += d

print(g, h)