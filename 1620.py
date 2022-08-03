import sys
N, M =  map(int,sys.stdin.readline().split())

name = [sys.stdin.readline().strip() for _ in range(N)]#포켓몬이름리스트
Q = [sys.stdin.readline().strip() for _ in range(M)]#문제리스트
for i in Q:
    if i.isnumeric(): #문제가 숫자면 이름리스트에서 인덱스로 이름 뽑기
        print(name[int(i)-1])
    else: #문제가 이름이면 이름리스트에서 이름으로 인덱스 번호 뽑아냄
        print((name.index(i)+1))
