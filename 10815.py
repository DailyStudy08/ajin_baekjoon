import sys

def bin_search(s,e,key):

    while s <= e:
        m = (s + e) // 2
        if arr[m] == key:
            return 1
        elif arr[m] > key:
            e = m-1
        else:
            s = m+1
    return 0

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
M = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
for i in lst:
    print(bin_search(0,N-1,i),end=' ')