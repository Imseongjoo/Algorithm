total = 0
for i in range(5):
    sc = int(input())
    if sc < 40:
        sc = 40
    total += sc
print(total // 5)