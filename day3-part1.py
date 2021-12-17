import numpy as np
from scipy import stats

file = np.loadtxt('day3-input.txt', dtype=str)
input = []
for i in range(0, len(file)):
    input.append([*file[i]])
input = np.array(input)
m = stats.mode(input)

gamma = 0
epsilon = 0

for i in range(len(m[0][0]), 0, -1):
    gam_val = int(m[0][0][i-1])
    eps_val = 0
    if gam_val == 0:
        eps_val = 1
    else:
        eps_val = 0
    power = len(m[0][0]) - i
    gamma += gam_val * 2**power
    epsilon += eps_val * 2**power

print (gamma * epsilon)