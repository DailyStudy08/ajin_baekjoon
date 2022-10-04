def dfs():
    if len(stack) == M:
        print(*stack,sep=' ')
        return
    for i in range(1,N+1):
        stack.append(i)
        dfs()
        stack.pop()

N, M = map(int, input().split())
stack = []
visit = []
dfs()