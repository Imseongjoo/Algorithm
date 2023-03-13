from collections import deque
import sys  # 속도 빠르게 하고 싶어서

n = int(sys.stdin.readline())
deque = deque()  # deque 선언

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':  # 'push_front'일때
        deque.appendleft(command[1])  # X를 deque의 앞에 넣는다
    elif command[0] == 'push_back':  # 'push_back'일때
        deque.append(command[1])  # X를 deque의 뒤에 넣는다

    elif command[0] == 'pop_front':  # 'pop_front'일때
        if len(deque) == 0:  # deque이 비었으면, -1 출력
            print(-1)
        else:  # 아니면 가장 앞의 정수를 pop
            print(deque.popleft())
    elif command[0] == 'pop_back':  # 'pop_back'일때
        if len(deque) == 0:  # deque이 비었으면, -1 출력
            print(-1)
        else:  # 아니면 가장 뒤의 정수를 pop
            print(deque.pop())

    elif command[0] == 'size':  # 'size'일때
        print(len(deque))  # deque 길이 출력
    elif command[0] == 'empty':  # 'empty'일때
        if len(deque) == 0:  # deque 길이가 0이면
            print(1)  # 1 출력
        else:
            print(0)  # 아니면 0 출력

    elif command[0] == 'front':  # 'front'일때
        if len(deque) == 0:  # deque 길이가 0이면
            print(-1)  # -1 출력
        else:
            print(deque[0])  # 아니면 가장 앞에 있는 정수 출력
    elif command[0] == 'back':  # 'back'일때
        if len(deque) == 0:  # deque 길이가 0이면
            print(-1)  # -1 출력
        else:
            print(deque[-1])  # 아니면 가장 뒤에 있는 정수 출력
