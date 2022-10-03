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
parent = [x for x in range(N)]
data = []
graph = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    data.append((x, y, z, i))
for i in range(3):
    data.sort(key=lambda x:x[i])
    for j in range(1, N):
        graph.append((abs(data[j-1][i]-data[j][i]), data[j-1][3], data[j][3]))
graph.sort()
sumV = 0
for w, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        sumV += w

print(sumV)