stack = []
N = int(input())
lst = [list(input().split()) for _ in range(N)]

for i in range(N):
    if lst[i][0]=='push':
        stack.append(lst[i][1])
    elif lst[i][0]=='pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif lst[i][0]=='size':    
        print(len(stack))
    elif lst[i][0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif lst[i][0]=='top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)