def dfs(s):
    if len(stack) == M:
        print(*stack,sep=' ')
        return
    for i in range(s,N+1):
        if i not in stack:
            stack.append(i)
            dfs(i+1)
            stack.pop()

N, M = map(int, input().split())
stack = []
visit = []
dfs(1)