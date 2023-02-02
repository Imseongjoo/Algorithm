f, v, p = map(int, input().split())
if v >= p:
    print(-1)
else:
    print((f//(p-v))+1)