N = int(input())
ls = []
for i in range(1,10000000):
    if '666' in str(i):
        ls.append(i)
dic = {i+1:ls[i] for i in range(len(ls))}
print(dic[N])