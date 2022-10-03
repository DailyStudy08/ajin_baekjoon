import sys

def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

N = int(sys.stdin.readline().strip())
data = [[] for _ in range(2)]
graph = []
parent = [x for x in range(N)]
for _ in range(N):
    x, y = map(float, sys.stdin.readline().split())
    data[0].append(x)
    data[1].append(y)
for i in range(N):
    for j in range(N):
        w = ((data[0][i]-data[0][j])**2+(data[1][i]-data[1][j])**2)**0.5
        graph.append((w, i, j))
graph.sort()

sumV = 0
for w, x, y in graph:
    if find(x) != find(y):
        union(x, y)
        sumV += w
print(round(sumV,2))
