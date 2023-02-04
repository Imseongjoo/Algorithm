N = int(input())
if N == 1:
    print()
a = []
i = 2
while N>=i:
    if N%i == 0:
        a.append(i)
        print(i) 
        N = N//i
        i = 2
    else:
        i += 1