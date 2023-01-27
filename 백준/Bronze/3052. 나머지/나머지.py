ls = []
for i in range(10):
    ls.append(int(input())%42)
res = set(ls)
print(len(res))