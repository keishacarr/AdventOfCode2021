with open ('day6-testinput.txt') as fin:
    data = fin.read().split(',')

allFish = [int(fish) for fish in data]

for day in range(0, 256):
    for i in range(0, len(allFish)):
        if allFish[i] == 0:
            allFish[i] = 6
            allFish.append(8)
        else:
            allFish[i] -= 1

print(len(allFish))