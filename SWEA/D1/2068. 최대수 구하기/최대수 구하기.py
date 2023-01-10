T = int(input())
for T in range(1, T+1):
    numbers = list(map(int,input().split()))
    a = max(numbers)
    print(f"#{T} {a}")