import itertools

class Amp:
    def __init__(self):
        self.code = [3,8,1001,8,10,8,105,1,0,0,21,38,59,84,93,110,191,272,353,434,99999,3,9,101,5,9,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,102,5,9,9,1001,9,4,9,1002,9,2,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99]
        self.ptr = 0

    def intcode(self, inputs):
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

        decoded = decode(self.code[self.ptr])
        op = decoded[0]

        while op != 99:
            if op < 3:
                v1 = self.code[self.ptr + 1] if 1 == decoded[1] else self.code[self.code[self.ptr + 1]]
                v2 = self.code[self.ptr + 2] if 1 == decoded[2] else self.code[self.code[self.ptr + 2]]
                pos = self.code[self.ptr + 3]

                if op == 1:
                    self.code[pos] = v1 + v2
                else:
                    self.code[pos] = v1 * v2

                self.ptr += 4

            elif op > 4:
                v1 = self.code[self.ptr + 1] if 1 == decoded[1] else self.code[self.code[self.ptr + 1]]
                v2 = self.code[self.ptr + 2] if 1 == decoded[2] else self.code[self.code[self.ptr + 2]]
                if op == 5 and v1 !=0:
                    self.ptr = v2
                elif op == 6 and v1 == 0:
                    self.ptr = v2
                elif op == 7:
                    pos = self.code[self.ptr + 3]
                    self.code[pos] = 1 if v1 < v2 else 0
                    self.ptr += 4
                elif op == 8:
                    pos = self.code[self.ptr + 3]
                    self.code[pos] = 1 if v1 == v2 else 0
                    self.ptr += 4
                else:
                    self.ptr +=3
            else:
                if op == 3:
                    tmp = inputs.pop(0)
                    self.code[self.code[self.ptr + 1]] = tmp
                    self.ptr += 2
                else:
                    self.ptr += 2
                    return(self.code[self.code[self.ptr - 1]])

            decoded = decode(self.code[self.ptr])
            op = decoded[0]
        return -1

def feedback(settings):
    value = 0
    out = 0
    amps = [Amp() for _ in settings]

    for i in range(len(amps)):
        value = amps[i].intcode([settings[i], value])

    step = 0

    while True:
        index = step % 5
        value = amps[index].intcode([value])
        if value == -1: 
            return out
        if index == 4:
            out = value
        step += 1

values = [feedback(list(settings)) for settings in itertools.permutations(range(5, 10))]
print(max(values))
