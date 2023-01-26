i = 0
r = [0, 0]
for c in input():
    if c == '@':
        r[i] += 1
    elif c == '(':
        i ^= 1
print(*r)