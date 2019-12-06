orbits = {}

with open('input.txt', 'r') as fp:
    line = fp.readline()
    while line:
        line = line.rstrip()
        objects = line.split(')')
        line = fp.readline()
        parent = objects[0]
        child = objects[1]
        orbits[child] = parent

def get_path(start):
    current = start
    path = []
    while (current != 'COM'):
        current = orbits[current]
        path.append(current)
    return path

transfers = set(get_path('YOU')).symmetric_difference(get_path('SAN'))

print(len(transfers))
