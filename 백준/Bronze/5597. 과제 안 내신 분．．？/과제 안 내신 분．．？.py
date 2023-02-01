A = []
B = []
for i in range(1,31):
    A.append(i)
for j in range(1,29):
    N = list(map(int, input().split()))
    for k in N:
        B.append(k)
C=set(A)
D=set(B)
E=C-D
print(min(E), max(E))