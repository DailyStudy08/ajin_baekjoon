students = [x for x in range(1,31)]
for i in range(28):
    n = int(input())
    students.remove(n)
print(*students,sep='\n')
