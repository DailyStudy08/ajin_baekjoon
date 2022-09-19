import sys
n = int(sys.stdin.readline().strip())
data = [sys.stdin.readline().split() for _ in range(n)]

oldest = {'name':'', 'd':32, 'm':13, 'y':2011}
youngest = {'name':'', 'd':0, 'm':0, 'y':0}

for i in range(n):
    if int(data[i][3]) < oldest['y']:
        oldest['name'] = data[i][0]
        oldest['d'] = int(data[i][1])
        oldest['m'] = int(data[i][2])
        oldest['y'] = int(data[i][3])
    if int(data[i][3]) == oldest['y']:
        if int(data[i][2]) < oldest['m']:
            oldest['name'] = data[i][0]
            oldest['d'] = int(data[i][1])
            oldest['m'] = int(data[i][2])
        elif int(data[i][2]) == oldest['m']:
            if int(data[i][1]) < oldest['d']:
                oldest['name'] = data[i][0]
                oldest['d'] = int(data[i][1])
    if int(data[i][3]) > youngest['y']:
        youngest['name'] = data[i][0]
        youngest['d'] = int(data[i][1])
        youngest['m'] = int(data[i][2])
        youngest['y'] = int(data[i][3])
    if int(data[i][3]) == youngest['y']:
        if int(data[i][2]) > youngest['m']:
            youngest['name'] = data[i][0]
            youngest['d'] = int(data[i][1])
            youngest['m'] = int(data[i][2])
        elif int(data[i][2]) == youngest['m']:
            if int(data[i][1]) > youngest['d']:
                youngest['name'] = data[i][0]
                youngest['d'] = int(data[i][1])
print(youngest['name'])
print(oldest['name'])
