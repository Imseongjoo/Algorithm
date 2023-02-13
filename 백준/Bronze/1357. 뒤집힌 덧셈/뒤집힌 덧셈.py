x, y = map(str,input().split())
a = (int(x[::-1])+int(y[::-1]))
b = str(a)[::-1]
print(int(b))