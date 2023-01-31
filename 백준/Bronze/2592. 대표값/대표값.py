N = [int(input()) for i in range(10)]
print((round(sum(N)/10)), max(N, key = N.count))