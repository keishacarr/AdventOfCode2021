input = []
for line in open('day2-input.txt'):
    item = line.rstrip('\n').split(' ')
    item[1] = int(item[1])
    input.append(item)
location = [0, 0, 0] # [horizontal, depth, aim]

for i in range(0, len(input)):
    if input[i][0] == "forward":
        location[0] = location[0] + input[i][1]
        location[1] = location[1] + location[2]*input[i][1]
    elif input[i][0] == "down":
        location[2] = location[2] + input[i][1]
    else: # direction is up
        location[2] = location[2] - input[i][1]

print (location[0] * location[1])