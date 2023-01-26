T = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]

while True:
    for i in range(len(T)-1):
        if T[i] > T[i+1]:
            T[i], T[i+1] = T[i+1], T[i]
            print(" ".join(map(str, T)))
    if T == answer:
        break