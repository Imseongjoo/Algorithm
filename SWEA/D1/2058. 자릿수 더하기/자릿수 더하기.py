n =  int(input())

if n < 0:
    print(-1)
else:
    result =0
    while n > 0:
        result += n%10
        n //= 10
    print(result)