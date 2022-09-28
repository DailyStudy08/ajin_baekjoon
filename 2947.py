import sys
arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(arr)

while arr != sorted_arr:
    for i in range(4):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            print(*arr)
