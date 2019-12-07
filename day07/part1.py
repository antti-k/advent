import itertools

code = [3,8,1001,8,10,8,105,1,0,0,21,38,59,84,93,110,191,272,353,434,99999,3,9,101,5,9,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,102,5,9,9,1001,9,4,9,1002,9,2,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99]

def intcode(code, inputs):
    def decode(ins):
        decoded = [0] * 4
        decoded[0] = ins % 100
        ins = ins // 100
        i = 1
        while ins > 0:
            decoded[i] = ins % 10
            ins = ins // 10
            i += 1

        return decoded

    ptr = 0
    decoded = decode(code[ptr])
    op = decoded[0]

    while op != 99:
        if op < 3:
            v1 = code[ptr + 1] if 1 == decoded[1] else code[code[ptr + 1]]
            v2 = code[ptr + 2] if 1 == decoded[2] else code[code[ptr + 2]]
            pos = code[ptr + 3]

            if op == 1:
                code[pos] = v1 + v2
            else:
                code[pos] = v1 * v2

            ptr += 4

        elif op > 4:
            v1 = code[ptr + 1] if 1 == decoded[1] else code[code[ptr + 1]]
            v2 = code[ptr + 2] if 1 == decoded[2] else code[code[ptr + 2]]
            if op == 5 and v1 !=0:
                ptr = v2
            elif op == 6 and v1 == 0:
                ptr = v2
            elif op == 7:
                pos = code[ptr + 3]
                code[pos] = 1 if v1 < v2 else 0
                ptr += 4
            elif op == 8:
                pos = code[ptr + 3]
                code[pos] = 1 if v1 == v2 else 0
                ptr += 4
            else:
                ptr +=3
        else:
            if op == 3:
                tmp = inputs.pop(0)
                code[code[ptr + 1]] = tmp
            else:
                return(code[code[ptr + 1]])
            ptr += 2

        decoded = decode(code[ptr])
        op = decoded[0]

def amplify(settings):
    value = 0
    for phase in settings:
        value = intcode(code, [phase, value])
    return value

values = [amplify(list(settings)) for settings in itertools.permutations(range(5))]
print(max(values))
