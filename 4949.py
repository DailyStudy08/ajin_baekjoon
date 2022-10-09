from collections import deque
import sys
while True:
    W = sys.stdin.readline()
    S = deque()

    if W == '.\n':
        break
    for w in W:
        if w == '(':
            S.append(w)
        elif w == ')':
            if S and S[-1] == '(':
                S.pop()
            else:
                print('no')
                break
        elif w == '[':
            S.append(w)
        elif w == ']':
            if S and S[-1] == '[':
                S.pop()
            else:
                print('no')
                break
    else:
        if S:
            print('no')
        else:
            print('yes')

