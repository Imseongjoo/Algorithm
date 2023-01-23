T = int(input())
if T%4 == 0 and (not T%100 == 0 or T%400 == 0):
    print(1)
else:
    print(0)