
import sys

A , B , V = map(int,sys.stdin.readline().split())

if A >= V : #하루에 올라갈수 있는 높이가 정상과 같거나 높아 하루만에 갈 수 있을 때
    print(1)

else:
    #첫 날 낮에 올라가고나서 정상까지 남은 높이가 다음날 다 갈 수 없을 때
    if (V-A) > (-B+A): 
        if (V-A)%(-B+A) == 0: 
            print((V-A)//(-B+A)+1)
        else:
            print((V-A)//(-B+A)+2)

    #첫 날 낮에 올라가고나서 정상까지 남은 높이가 다음날 다 갈 수 있을 때        
    else:
        print(2)
