N = int(input())
ls = list(map(int, input().split()))
a = max(ls)
b = []
for i in ls:
    b.append(i/a*100)
print(sum(b)/N)