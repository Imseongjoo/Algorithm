string = input()
ls = string.split(',')
nls = list(map(int, ls))
print(sum(nls))