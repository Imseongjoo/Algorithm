a=[list(input().split()) for _ in range(4)]
b = []
cnt = 0
for i in range(4):
        cnt -= (int(a[i][0]))
        b.append(cnt)  
        cnt += (int(a[i][1]))
        b.append(cnt)         
print(max(b))