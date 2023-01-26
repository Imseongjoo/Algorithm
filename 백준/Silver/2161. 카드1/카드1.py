N = int(input())
queue = list(range(1,N+1))
dis = []
while len(queue) > 1:
    dis.append(queue.pop(0))
    queue.append(queue.pop(0))
print(*dis, *queue)