input = []
for line in open('day2-input.txt'):
    item = line.rstrip('\n').split(' ')
    item[1] = int(item[1])
    input.append(item)
loc = [0,0]

for i in range(0, len(input)):
    if input[i][0] == "forward":
        loc[0] = loc[0] + input[i][1]
    elif input[i][0] == "down":
        loc[1] = loc[1] + input[i][1]
    else: # direction is up
        loc[1] = loc[1] - input[i][1]

print (loc[0] * loc[1])