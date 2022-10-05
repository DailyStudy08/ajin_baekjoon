import sys
N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
arr_dict = {}
for i in range(N):
    if arr[i] in arr_dict:
        arr_dict[arr[i]] += 1
    else:
        arr_dict[arr[i]] = 1

M = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    if arr_dict.get(data[i]):
        print(arr_dict.get(data[i]),end=' ')
    else:
        print(0,end=' ')
