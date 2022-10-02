import sys
def find(x):
    if parents[x] == x:
        return x
    p = find(parents[x])
    parents[x] = p
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[y] = x
        friends[x] += friends[y]
    else:
        return

T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())
    parents = {}
    friends = {}
    for _ in range(F):
        x, y = sys.stdin.readline().split()
        if x not in parents:
            parents[x] = x
            friends[x] = 1
        if y not in parents:
            parents[y] = y
            friends[y] = 1
        union(x, y)
        print(friends[find(x)])