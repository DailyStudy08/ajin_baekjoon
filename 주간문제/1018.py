chess1 =[
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB']

chess2 =[
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW']

N,M = map(int, input().split())
board = [input() for _ in range(N) ]
minV = []
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt1 = 0
        cnt2 = 0
        for k in range(8):
            for l in range(8):
                if board[k+i][l+j] != chess1[k][l]:
                    cnt1 += 1
                if board[k+i][l+j] != chess2[k][l]:
                    cnt2 += 1

        minV.append(cnt1)
        minV.append(cnt2)

print(min(minV))