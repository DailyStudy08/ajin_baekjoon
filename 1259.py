import sys

while True:
    c = sys.stdin.readline().strip()
    if c == '0':
        break
    if c == c[::-1]:
        print('yes')
    else: 
        print('no')