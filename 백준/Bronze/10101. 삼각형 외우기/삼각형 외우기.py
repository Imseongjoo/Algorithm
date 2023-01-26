a=int(input())
b=int(input())
c=int(input())
if a == b == c == 60:
    print('Equilateral')
elif a+b+c == 180 and a == b:
    print('Isosceles')
elif a+b+c == 180 and a == c:
    print('Isosceles')
elif a+b+c == 180 and b == c:
    print('Isosceles')
elif a+b+c == 180 and a != b != c:
    print('Scalene')
elif a+b+c != 180:
    print('Error')