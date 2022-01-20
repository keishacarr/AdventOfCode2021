from collections import Counter

with open ('day5-input.txt') as fin:
    data = fin.read().splitlines()

allPoints = []
for line in data:
    firstPoint, secondPoint = line.split('->')
    x1, y1 = tuple(map(int, firstPoint.split(',')))
    x2, y2 = tuple(map(int, secondPoint.split(',')))

    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                allPoints.append((x, y))
    else:
        xinc = 1 if x1 < x2 else -1
        yinc = 1 if y1 < y2 else -1
        y = y1
        for x in range (x1, x2+xinc, xinc):
            allPoints.append((x, y))
            y += yinc

print(len([point for point in Counter(allPoints).values() if point > 1]))