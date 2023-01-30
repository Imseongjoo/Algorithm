A, B = input().split()
a = []
b = []
for i in str(A):
    a.append(i)
for j in str(B):
    b.append(j)
cnt = 0
for k in a:
    for l in b:
        cnt += int(k)*int(l)
print(cnt)