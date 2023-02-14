from collections import Counter

ls = []
for _ in range(int(input())):
    num = int(input())
    ls.append(num)

ls.sort()

cnt = Counter(ls).most_common(2)

print(round(sum(ls) / len(ls)))
print(ls[len(ls)//2])
if len(ls) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(ls)-min(ls))