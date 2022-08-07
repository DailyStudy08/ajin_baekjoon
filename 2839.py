import sys

N = int(sys.stdin.readline())

if N % 5 == 0: #5kg 짜리로 모두 가져갈 수 있을 때
    print(N//5)

else: 
    for i in range(N//5,-1,-1): #5kg을 최대로 하기위해 i가 점점 작아지게 범위 잡음
        if (N-(5*i)) % 3 == 0: #5kg 짜리로 i 개 가져가고 나머지 무게가 3kg으로 딱 떨어질 때
            result = i + (N-(5*i)) // 3
            print(result)
            break
    else:
        print(-1) #정확하게 N킬로그램으로 만들 수 없을 때, 위에서 브레이크 없을 때