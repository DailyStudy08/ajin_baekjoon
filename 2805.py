import sys
def bin(s,e,key):
    while True:
        m = (s+e) // 2
        tree = 0
        for i in trees:
            if i-m > 0:
                tree += i-m
        if tree == key or s>e:
            return m
        elif tree > key:
            s = m+1
        elif tree < key:
            e = m-1


N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
s = 0
e = max(trees)
result = bin(s,e,M)
print(result)
