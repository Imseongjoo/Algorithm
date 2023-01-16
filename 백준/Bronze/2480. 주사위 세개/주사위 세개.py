A, B, C = map(int, input().split())
if A == B == C:
    print((A*1000)+10000)
elif A == B or B == C:
    print(1000+B*100)
elif A == C:
    print(1000+A*100)
else:
    print(max(A,B,C)*100)