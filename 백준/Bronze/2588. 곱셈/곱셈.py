a = int(input())
b = int(input())
c = (a*(b%10))
d = (a*((b%100-b%10)/10))
e = (a*((b-b%100)/100))
print(a*(b%10))
print(round(a*((b%100-b%10)/10)))
print(round(a*((b-b%100)/100)))
print(round(c+(10*d)+(100*e)))