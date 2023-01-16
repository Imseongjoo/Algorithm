N = int(input())
C = 0
NC = 0
for i in range(1, N+1):
    A = int(input())
    if A == 0:
        NC += 1
    else:
        C += 1
if C>NC:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")