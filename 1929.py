import math

n = 1000000
arr = [1 for i in range(n+1)]
arr[1] = 0

for i in range(2,int(math.sqrt(n))+1):
    if arr[i]:
        j = 2
        while i*j <= n:
            arr[i*j] = 0
            j += 1

M, N = map(int,input().split())
for i in range(M, N+1):
    if arr[i]:
        print(i)