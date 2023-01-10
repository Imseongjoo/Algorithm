T = int(input())
for T in range(1, T+1):
    numbers = list(map(int,input().split()))
    a = sum(numbers)/len(numbers)
    a = round(a)
    print(f"#{T} {a}")