import sys

N, M= map(int,sys.stdin.readline().split())
ps = [sys.stdin.readline().strip() for _ in range(N)]
ss = [sys.stdin.readline().strip() for _ in range(M)]

cnt = 0
for i in ss:
    if i in set(ps):
        cnt += 1
print(cnt)