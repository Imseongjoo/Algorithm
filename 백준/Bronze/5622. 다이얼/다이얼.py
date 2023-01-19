number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alpha = input()
time = 0
for i in range(len(alpha)):
    for j in number:
        if alpha[i] in j:
            time += number.index(j)+3
print(time)