import sys

def find(x):
    if parents[x] == x:
        return x
    p = find(parents[x])
    parents[x] = p
    return parents[x]

def union(x, y):
    if find(x) == find(y):
        return 1
    if find(x) > find(y):
        parents[find(x)] = find(y)
    else:
        parents[find(y)] = find(x)

n, m = map(int, sys.stdin.readline().split())
parents = [x for x in range(n)]
data = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
for i in range(m):
    x, y = data[i][0], data[i][1]
    ans = union(x, y)
    if ans:
        print(i+1)
        break
else:
    print(0)