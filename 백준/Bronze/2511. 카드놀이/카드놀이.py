import sys
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
cnta = 0
cntb = 0

for i in range(10):
    if a[i] == b[i]:
        cnta += 1
        cntb += 1
    elif a[i] > b[i]:
        cnta += 3
    else:
        cntb += 3

if cnta > cntb:
    print(cnta, cntb)
    print('A')
    
elif cnta < cntb:
    print(cnta, cntb)
    print('B')

else:
    j = -1
    while j > -10:
        if a[j] > b[j]:
            print(cnta, cntb)
            print('A')
            break
        elif a[j] < b[j]:
            print(cnta, cntb)
            print('B')
            break
        elif a[j] == b[j]:
            j -= 1
            continue

        if a[j] > b[j]:
            print(cnta, cntb)
            print('A')
        elif a[j] < b[j]:
            print(cnta, cntb)
            print('B')
    else:
        try:
            print(cnta, cntb)
            print('D')
        except:
            print(cnta, cntb)
            print('D')