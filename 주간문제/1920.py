import sys

def S(a,N,key):
    s = 0
    e = N-1
    while s <= e:
        if key > a[(s+e)//2]:
            s = (s+e)//2+1
            
        elif key < a[(s+e)//2]:
            e = (s+e)//2-1
           
        else:
            return 1
    return 0

N = int(sys.stdin.readline().strip())
n = sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline().strip())
m = list(map(int,sys.stdin.readline().split()))

for i in range(M):
    print(S(n,N,m[i]))
    