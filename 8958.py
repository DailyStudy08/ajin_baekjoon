import sys

N = int(sys.stdin.readline().strip())
for i in range(N):
    case = sys.stdin.readline().strip()

    cnt = 0
    cnt_list = [0]*len(case)
    for i in range(len(case)):
        if case[i] == 'O':
            cnt += 1
            cnt_list[i] = cnt
        else:
            cnt = 0
            cnt_list[i] = 0

    print(sum(cnt_list))
