with open('input.txt', 'r') as fp:
    line = fp.readline()
    sum = 0
    while line:
        fuel = int(line.strip()) // 3 - 2
        while (fuel > 0):
            sum += fuel
            fuel = fuel // 3 - 2
        line = fp.readline()
        

    print(sum) 

