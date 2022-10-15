N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-1,-1,-1):
    if K//arr[i] > 0:
        n = K//arr[i]
        K -= n * arr[i]
        cnt += n
print(cnt)