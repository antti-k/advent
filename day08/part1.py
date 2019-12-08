with open('input.txt', 'r') as fp:
    line = fp.readline()
    pixels = [int(char) for char in line.rstrip()]
    batch_size = 25 * 6
    layers = []

    for i in range(len(pixels) / batch_size):
        layer_start = i * batch_size
        layers.append(pixels[layer_start:layer_start + batch_size])

    zero_counts = map(lambda l: l.count(0), layers)
    index = zero_counts.index(min(zero_counts))

    checksum = layers[index].count(1) * layers[index].count(2)
    print(checksum)



    
