import sys
N,M = map(int,sys.stdin.readline().split())
A = {sys.stdin.readline().strip() for _ in range(N)}
B = {sys.stdin.readline().strip() for _ in range(M)}

C = sorted(A & B)
print(len(C))
print(*C,sep='\n')