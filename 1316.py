import sys
N = int(sys.stdin.readline())

lst = [sys.stdin.readline().strip() for _ in range(N)] #단어들 모든 리스트
cnt = 0
for i in lst:
    data = set()
    # 단어에서 알파벳 하나씩 뽑아서 data에 안들어 있으면 넣고, 
    # data에 이미 있을 때 바로 전 알파벳과 비교해서 서로 같지 않으면 연속된 게 아니라는 뜻이므로 break
    # break 없이 끝나면 cnt + 1
    for j in range(len(i)): 
        if i[j] not in data:
            data.add(i[j])
        elif i[j] in data and i[j] != i[j-1] :
            break
    else: cnt += 1
print(cnt)


      