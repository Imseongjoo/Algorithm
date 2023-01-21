N = int(input())
cnt = N
for i in range(N):
    string = input()
    for j in range(0, len(string)-1):
        if string[j] == string[j+1]:
            pass
        elif string[j] in string[j+1:]:
            cnt -= 1
            break
print(cnt)