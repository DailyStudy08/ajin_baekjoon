from collections import deque
import sys

N = int(sys.stdin.readline())
q = deque()
for i in range(N):
    data = sys.stdin.readline().split()
    if data[0] == 'push_front':
        q.appendleft(data[1])
    elif data[0] == 'push_back':
        q.append(data[1])
    elif data[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif data[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(q))
    elif data[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif data[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif data[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)