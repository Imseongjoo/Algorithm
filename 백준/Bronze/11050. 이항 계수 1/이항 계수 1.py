N,K=map(int, input().split())
ja = 1
mo = 1
for i in range(N,N-K,-1):
    ja *= i
for j in range(K,0,-1):
    mo *= j
print(ja//mo)