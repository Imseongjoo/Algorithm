while True:
    n,m = map(int, input().split())
    if n>m and n%m == 0:
        print('multiple')
    elif m>n and m%n == 0:
        print('factor')
    elif (n == 0 and m == 0):
        break
    elif n and m != 0:
        print('neither')