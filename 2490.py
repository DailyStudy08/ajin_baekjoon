for _ in range(3):
    data = list(input().split())
    cnt = data.count('0')
    if cnt == 0:
        print('E')
    elif cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')

