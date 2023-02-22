N = int(input())
a = []
for i in range(1,2*N):
    if i<=N:
        a.append(f"{(N-i)*' '}{'*'*(2*i-1)}")
        print(f"{(N-i)*' '}{'*'*(2*i-1)}")
    elif i>N:
        print(a[N-i-1])