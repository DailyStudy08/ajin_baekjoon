import sys

N = int(sys.stdin.readline())

word = {sys.stdin.readline().strip() for i in range(N)}

lst = sorted(word, key= lambda x : (len(x),x),)

print(*lst, sep='\n')