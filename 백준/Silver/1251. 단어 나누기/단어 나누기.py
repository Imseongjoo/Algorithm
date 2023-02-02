string = list(input())
cnt = []
ans = []
for i in range(1,len(string)-1):
    for j in range(i+1,len(string)):
        a = string[:i]
        b = string[i:j]
        c = string[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        cnt.append(a+b+c)
for k in cnt:
    ans.append(''.join(k))
print(sorted(ans)[0])