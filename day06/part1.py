orbits = {}

with open('input.txt', 'r') as fp:
    line = fp.readline()
    while line:
        line = line.rstrip()
        objects = line.split(')')
        line = fp.readline()
        parent = objects[0]
        child = objects[1]
        if parent in orbits:
            orbits[parent] += [child]
        else:
            orbits[parent] = [child]

def orbit_count(parent, depth = 0):
    if parent in orbits:
        children = orbits[parent]
        return depth + sum([orbit_count(child, depth + 1) for child in orbits[parent]])
    else:
        return depth

print(orbit_count('COM'))

