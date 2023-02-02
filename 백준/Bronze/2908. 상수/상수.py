a,b= map(int, input().split())
aa= str(a)[::-1]
bb = str(b)[::-1]
if aa > bb:
    print(aa)
else:
    print(bb)