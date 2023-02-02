n = input().lower()
ls = list(set(n))
cnt = []

for i in ls:
    c = n.count(i)
    cnt.append(c)

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(ls[(cnt.index(max(cnt)))].upper())