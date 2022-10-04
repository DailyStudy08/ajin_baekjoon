def dfs():
    if len(stack) == M:
        print(*stack,sep=' ')
        return
    for i in range(1,N+1):
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()

N, M = map(int, input().split())
stack =[]
dfs()