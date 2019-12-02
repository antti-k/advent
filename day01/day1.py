import math
with open('input.txt', 'r') as fp:
    line = fp.readline()
    sum = 0
    while line:
        fuel = math.floor(int(line.strip())/3) - 2
        while (fuel > 0):
            sum += fuel
            fuel = math.floor(fuel/3) - 2
        line = fp.readline()
        

    print(sum) 

