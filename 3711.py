import sys

N = int(sys.stdin.readline().strip()) #테스트케이스 개수
for _ in range(N):
    G = int(sys.stdin.readline().strip()) #학생수
    num = [int(sys.stdin.readline().strip()) for _ in range(G)] #학번 리스트
    if len(num) == 1: # 학번 1개면 가장 작은 나머지는 1로 나눈 나머지 0 이므로 답은 1
        print(1)
    else:
        for i in range(1,1000000): # 1부터 숫자를 증가시켜가며 학번들을 나누고,
            remain=set()
            for j in num:
                remain.add(j%i) # 나눈 나머지를 세트(remain)에 넣는다
            if len(remain) == len(num):  # 세트의 길이와 학번리스트(num) 같다면 성공
                break  # 가장 작은 값을 구했으므로 break