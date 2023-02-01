numbers = set(range(1,10001))
rmv = set()
for i in numbers:
    for j in str(i):
        i += int(j)
    rmv.add(i)
sel = numbers-rmv
for k in sorted(sel):
    print(k)