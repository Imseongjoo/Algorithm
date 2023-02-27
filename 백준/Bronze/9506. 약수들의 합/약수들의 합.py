while True:
    n = int(input())
    if n == -1:
        break
    a = []
    for i in range(1, round(n/2) + 1):
        if n % i == 0:
            a.append(i)
    if sum(a) == n:
        print(f"{n} = {' + '.join(map(str,a))}")
    else:
        print(f"{n} is NOT perfect.")