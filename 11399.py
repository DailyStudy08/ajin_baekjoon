import sys
N = int(sys.stdin.readline().strip())
arr = list(map(int, (sys.stdin.readline().split())))
arr.sort()
for i in range(1, N):
    arr[i] = arr[i]+arr[i-1]

print(sum(arr))