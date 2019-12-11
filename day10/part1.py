full_asteroids = []

with open('input.txt', 'r') as fp:
    line = fp.readline()
    while line:
        tmp = [char for char in line.rstrip()]
        row = map(lambda a: True if a == '#' else False, tmp)
        full_asteroids.append(row)
        line = fp.readline().rstrip()

stations = []
height = len(full_asteroids)
width = len(full_asteroids[0])
for row in range(height):
    for column in range(width):
        if full_asteroids[row][column]:
            stations.append([column, row])
            
def los_count(coords):
    x = coords[0]
    y = coords[1]
    asteroids_above = full_asteroids[:y]
    asteroids_below = full_asteroids[y + 1:]
    row = full_asteroids[y]
    count =  above(x, asteroids_above) + below(x, asteroids_below) + same_row(x, row)
    return count


def above(x, asteroids):
    height = len(asteroids)
    if height == 0:
        return 0
    width = len(asteroids[0])
    coords = []

    for row in range(height):
        for column in range(width):
            if asteroids[row][column]:
                coords.append((column - x) * 1.0 / (height - row * 1.0))

    count = len(set(coords))
    return count

def below(x, asteroids):
    height = len(asteroids)
    if height == 0:
        return 0
    width = len(asteroids[0])
    coords = []

    for row in range(height):
        for column in range(width):
            if asteroids[row][column]:
                coords.append((column - x) * 1.0 / (row + 1))

    count = len(set(coords))
    return count

def same_row(x, row):
    before = True in row[:x] * 1
    after = True in row[x + 1:] * 1

    return before + after

los_counts = map(lambda coords: los_count(coords), stations)
print(max(los_counts))
