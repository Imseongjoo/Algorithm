T = int(input())

for i in range(T):
    stack = []
    S = input()
    for j in S:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: 
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')