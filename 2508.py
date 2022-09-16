T = int(input())

for tc in range(T):
    input()
    r,c = map(int,input().split())
    case = [input() for _ in range(r)]
    turn_case = ['']*c
    cnt = 0
    for i in range(c):
        for j in range(r):
            turn_case[i] += case[j][i]

    for i in range(c):
        cnt += turn_case[i].count('vo^')

    
    for i in range(r):
        cnt += case[i].count('>o<')

    print(cnt)