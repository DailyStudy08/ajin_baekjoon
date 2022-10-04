def dfs(s):
    if len(stack) == M:
        print(*stack,sep=' ')
        return
    for i in range(s,N+1):
        stack.append(i)
        dfs(i)
        stack.pop()

N, M = map(int, input().split())
stack = []
visit = []
dfs(1)