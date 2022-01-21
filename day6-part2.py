from collections import defaultdict

with open ('day6-input.txt') as fin:
    data = fin.read().split(',')

allFish = [int(fish) for fish in data]

fishMap = {}
for fish in allFish:
    if fish not in fishMap:
        fishMap[fish] = 0
    fishMap[fish] += 1

print(fishMap)

for day in range (0, 256):
    updatedFishMap = defaultdict(int)

    for fish, count in fishMap.items():
        if fish == 0:
            updatedFishMap[6] += count
            updatedFishMap[8] += count
        else:
            updatedFishMap[fish-1] += count
        
        fishMap = updatedFishMap
print(sum(fishMap.values()))

#print(len(allFish))