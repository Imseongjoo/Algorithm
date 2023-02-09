a,b=map(int, input().split())
c=[]
for i in range(1,a+1):
    for j in range(1,b+1):
        if a%i == 0:
            if b%j == 0:
                if i == j:
                    c.append(i)
print(max(c))
print(int((a*b)/max(c)))
                