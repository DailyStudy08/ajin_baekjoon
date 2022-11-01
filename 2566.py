arr = [list(map(int,input().split())) for _ in range(9)]
maxV = 0
maxI = 0
maxJ = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >= maxV:
            maxV, maxI, maxJ = arr[i][j], i, j
print(maxV)
print(maxI+1, maxJ+1)