while True:
    n=int(input())

    if n==0:
        break
    else:
        words = [input() for i in range(n)]

    sorted_words = []
    for i in range(n):
        sorted_words.append(words[i].lower())
    sorted_words.sort()
    for i in range(n):
        if words[i].lower() == sorted_words[0]:
            print(words[i])