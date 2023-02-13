from collections import Counter
N = int(input())
sale = []
for i in range(N):
   sale.append(input())
a = Counter(sale)
for key, value in sorted(a.items()):
    if value == max(a.values()):
        print(key)
        break