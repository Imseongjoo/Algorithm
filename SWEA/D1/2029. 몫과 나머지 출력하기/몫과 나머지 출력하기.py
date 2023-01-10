T = int(input())
for T in range(1, T+1):
    a, b = list(map(int,input().split()))
    q = a//b
    r = a%b
    print(f"#{T} {q} {r}")