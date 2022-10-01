import sys

K, N = map(int,sys.stdin.readline().split())
arr = [0]*K
for i in range(K):
    arr[i] = int(sys.stdin.readline().strip())
num = max(arr)
s = 1
e = num
mid = num//2

while s <= e:  # 가장 긴 것을 찾기 위해 s와 e가 만날 때 까지 계속한다.
    mid = (s + e) // 2
    cnt = 0
    for n in arr:
        cnt += n//mid
    if cnt >= N:  # cnt가 N과 같아도 가장 긴 것을 찾아야 하므로 계속 진행
        s = mid+1
    else:
        e = mid-1
print(e)