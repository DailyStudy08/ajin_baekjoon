import sys

def find(x):
    if parents[x] == x:
        return x
    p = find(parents[x])
    parents[x] = p
    return parents[x]

def union(x, y):
    if find(x) > find(y):
        parents[find(x)] = find(y)
    else:
        parents[find(y)] = find(x)

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
parents = [x for x in range(N+1)]
city = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if city[i][j]:
            union(i, j)
for k in range(1, M):
    if parents[plan[k-1]-1] != parents[plan[k]-1]:
        print('NO')
        break
else:
    print('YES')