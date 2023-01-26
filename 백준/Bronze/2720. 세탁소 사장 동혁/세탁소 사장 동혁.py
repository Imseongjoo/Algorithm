T = int(input())
for i in range(T):
    C = int(input())
    a = C//25
    b = (C%25)//10
    c = round((C-(25*a)-(10*b))//5)
    d = (C-(25*a)-(10*b)-(5*c))//1
    print(a, b, c, d)