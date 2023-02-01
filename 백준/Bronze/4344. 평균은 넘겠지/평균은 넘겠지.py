C = int(input())
for i in range(C):
    a = list(map(int, input().split()))
    s = sum(a[1:])/a[0]
    cnt = 0
    for j in a[1:]:
        if j > s:
            cnt += 1   
    b = (cnt/(a[0]))*100
    print(f"{b:.3f}%")