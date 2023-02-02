w = [list(map(int, input().split())) for i in range(10)]
k = [list(map(int, input().split())) for i in range(10)]
w.sort(key=lambda x: (x[0]))
k.sort(key=lambda x: (x[0]))
www = w[7][0]+w[8][0]+w[9][0]
kkk = k[7][0]+k[8][0]+k[9][0]
print(www,kkk)