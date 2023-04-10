n = int(input())
p = list(map(int, input().split()))

p.sort()

result = 0
time = []
for i in range(n):
    result += p[i]
    time.append(result)
print(sum(time))