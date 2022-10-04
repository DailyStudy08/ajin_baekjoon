import sys
N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = list(set(arr))
sorted_arr.sort()
arr_dict = {}
for i in range(len(sorted_arr)):
    arr_dict[sorted_arr[i]] = i
for i in arr:
    print(arr_dict[i],end=' ')

