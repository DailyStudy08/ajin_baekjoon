import sys
n = int(sys.stdin.readline().strip())
for _ in range(n):
    data = sys.stdin.readline().strip()
    r = int(len(data)**(1/2))
    letter = []
    for i in range(r):
        letter.append(data[i*r:i*r+r])
    for j in range(r):
        for k in range(r):
            print(letter[k][r-1-j],end='')
    print()



    #
    # print(r)