C = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
T = input()
for i in C :
    T = T.replace(i, 'a')
print(len(T))