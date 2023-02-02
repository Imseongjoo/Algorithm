M = int(input())
cup = [0,1,2,3]
for i in range(1,M+1):
    x,y = map(int, input().split())
    cup[x],cup[y]=cup[y],cup[x]
print(cup.index(1))