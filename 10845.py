queue = []
N = int(input())
lst = [list(input().split()) for _ in range(N)]

for i in range(N):
    if lst[i][0]=='push':
        queue.append(lst[i][1])
    elif lst[i][0]=='pop':
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif lst[i][0]=='size':    
        print(len(queue))
    elif lst[i][0]=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif lst[i][0]=='front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif lst[i][0]=='back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)