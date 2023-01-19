num1 = int(input())
num2 = int(input())
num3 = int(input())
result = list(str(num1 * num2 * num3))
for i in range(10):
    print(result.count(str(i)))