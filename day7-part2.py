with open ('day7-input.txt') as fin:
    data = [int(item) for item in fin.read().strip().split(',')]

start = min(data)
end = max(data)
sums = []

for i in range (start, end):
    sum = 0
    for elem in data:
        diff = abs (i-elem)
        sum += diff * (diff+1) / 2
    sums.append(sum)

val, idx = min((val, idx) for (idx, val) in enumerate(sums))
print ("position", idx, "uses the least fuel,", val)