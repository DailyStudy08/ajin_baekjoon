N, S = map(int, input().split())
arr = list(map(int, input().split()))
cntV = 0
for i in range(1 << N):
    sumV = 0

    for j in range(N):
        if i & (1 << j):
            sumV += arr[j]
    if sumV == S:
        cntV +=1
if S == 0:
    print(cntV-1)
else:
    print(cntV)