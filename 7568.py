N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    cnt = 1
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    print(cnt,end=' ')



