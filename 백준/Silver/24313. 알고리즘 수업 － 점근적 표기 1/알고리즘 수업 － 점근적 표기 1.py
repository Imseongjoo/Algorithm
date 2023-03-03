a1, a0 = map(int, input().split())  # a1과 a0 입력 받기
c = int(input())  # c 입력 받기
n0 = int(input())  # n0 입력 받기

for n in range(n0, 101):  # 1부터 100까지의 n에 대해서 반복
    if a1*n + a0 > c*n:  # 만약 f(n) > c * g(n)이라면
        print(0)  # 0 출력하고
        break  # 반복문을 빠져나옴
else:  # for문이 정상적으로 종료되었다면
    print(1)  # 1 출력