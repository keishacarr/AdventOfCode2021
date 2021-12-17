import numpy as np

file = np.loadtxt('day3-input.txt', dtype=str)
input = []
for i in range(0, len(file)):
    input.append([*file[i]])

#o2 generator
o2 = np.array(input)
bit_index = 0

while len(o2) > 1:
    bit = o2[:,bit_index]
    num0 = 0
    num1 = 0
    saved = 0
    
    # determine number of 0's and number of 1's in the bit
    for j in range(0, len(bit)):
        if int(bit[j]) == 0:
            num0 += 1
        elif int(bit[j]) == 1:
            num1 += 1

    # only change saved if there are more 0's than 1's
    if num1 >= num0:
        saved = 1

    #if row matches saved, add to temp array
    o2_temp = np.empty((0, len(o2[0])), int)
    for k in range (0, len(bit)):
        if int(bit[k]) == saved:
            o2_temp = np.append(o2_temp, [o2[k]], axis=0)
    
    o2 = o2_temp
    bit_index += 1


#co2 scrubber
co2 = np.array(input)
bit_index = 0

while len(co2) > 1:
    bit = co2[:,bit_index]
    num0 = 0
    num1 = 0
    saved = 0
    
    # determine number of 0's and number of 1's in the bit
    for j in range(0, len(bit)):
        if int(bit[j]) == 0:
            num0 += 1
        elif int(bit[j]) == 1:
            num1 += 1

    # only change saved if there are fewer 0's than 1's
    if num1 < num0:
        saved = 1

    #if row matches saved, add to temp array
    co2_temp = np.empty((0, len(co2[0])), int)
    for k in range (0, len(bit)):
        if int(bit[k]) == saved:
            co2_temp = np.append(co2_temp, [co2[k]], axis=0)
    
    co2 = co2_temp
    bit_index += 1

o2_dec = 0
co2_dec = 0
for i in range(len(o2[0]), 0, -1):
    o2_val = int(o2[0][i-1])
    co2_val = int(co2[0][i-1])

    power = len(o2[0]) - i
    o2_dec += o2_val * 2**power
    co2_dec += co2_val * 2**power

print(o2_dec * co2_dec)