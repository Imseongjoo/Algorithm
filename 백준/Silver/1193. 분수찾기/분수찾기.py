x = int(input())
ls = []
num = 0
cnt = 0
while cnt < x:
    num += 1
    cnt += num
cnt -= num
if num % 2 == 0:
    i = x - cnt
    j = num - i + 1
else:
    i = num - (x - cnt) + 1
    j = x - cnt
print(f"{i}/{j}")