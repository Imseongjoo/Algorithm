result = 0
ls = []
for i in range(7):
    num =int(input())
    if num % 2 != 0:
        ls.append(int(num))
    else:
        pass
if sum(ls) == 0:
    print(-1)
else:
    print(sum(ls))
    print(min(ls))