def validate(number):
    prev = number % 10
    number = number // 10
    adj_flag = False

    while (number > 0):
        current = number % 10
        if (current == prev):
            adj_flag = True
        elif (current > prev):
            return False

        prev = current
        number = number // 10

    return adj_flag

def validate2(number):
    prev = number % 10
    number = number // 10
    adjs = []
    adj_count = 1

    while (number > 0):
        current = number % 10
        if (current == prev):
            adj_count += 1
        elif (current > prev):
            return False
        else:
            adjs.append(adj_count)
            adj_count = 1

        prev = current
        number = number // 10

    adjs.append(adj_count)

    return 2 in adjs


possible_values = filter(validate, range(278384, 824795 + 1))
print(len(possible_values))

possible_values2 = filter(validate2, range(278384, 824795 + 1))
print(len(possible_values2))
