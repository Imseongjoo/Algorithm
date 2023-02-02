T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    a=[[0 for i in range(n)]for i in range(k+1)]
    for q in range(n):
        a[0][q] = q+1 
    for j in range(1,k+1):
        for z in range(n):
            a[j][z] += sum(a[j-1][:z+1])
    print(a[k][n-1])