N = int(input())
cnt = 0
string = 666
while True:
    if '666' in str(string):
        cnt += 1
    if cnt == N:
        print(string)
        break
    string += 1