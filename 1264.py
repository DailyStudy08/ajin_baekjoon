import sys

while True:

    word = sys.stdin.readline().strip()
    a= 'aeiouAEIOU'
    cnt = 0
    if word == '#':
        break
    for i in word:
        for j in a:
            if j == i:
                cnt += 1
    
    print(cnt)

