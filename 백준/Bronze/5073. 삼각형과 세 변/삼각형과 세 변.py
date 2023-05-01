while 1:
    a = list(map(int, input().split()))
    a.sort()
    if sum(a) == 0:
        break
    if a[0] + a[1] <= a[2]:
        print('Invalid')
    elif a[0] == a[1] == a[2]:
        print('Equilateral')
    elif a[0] != a[1] != a[2] != a[0]:
        print('Scalene')
    else:
        print('Isosceles')