import sys

board = sys.stdin.readline()

result = []
cnt = 0
for i in range(len(board)):
    if board[i] == 'X':
        cnt += 1
    elif board[i] == '.' or board[i] == '\n':
        if cnt == 0:
            if board[i] == '.':
                result.append('.')
        elif cnt % 2 == 1:
            print(-1)
            break
        elif cnt % 4 == 0:
            result.append((cnt//4)*'AAAA')
            if board[i] == '.':
                result.append('.')
            cnt = 0
        elif cnt % 4 == 2:
            result.append((cnt//4)*'AAAA'+'BB')
            if board[i] == '.':
                result.append('.')
            cnt = 0
else:
    print(*result, sep='')




