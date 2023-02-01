T = int(input())
for i in range(T):
    ls = list(map(int, input().split()))
    a = []
    lss = []
    for j in ls:
        lss.append(j)
    lss.remove(min(lss))
    lss.remove(max(lss))
    if (min(lss)+4) <= max(lss):
        print('KIN')
    else:
        a = sum(ls)-max(ls)-min(ls)
        print(a)