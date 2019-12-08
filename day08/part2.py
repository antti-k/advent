with open('input.txt', 'r') as fp:
    line = fp.readline()
    pixels = [int(char) for char in line.rstrip()]
    batch_size = 25 * 6
    layers = []

    for i in range(len(pixels) / batch_size):
        layer_start = i * batch_size
        layers.append(pixels[layer_start:layer_start + batch_size])

    image = [] 
    for i in range(batch_size):
        pixel = layers[0][i]
        j = 1
        while(pixel == 2):
            pixel = layers[j][i]
            j += 1
        image.append(pixel)

    for i in range(6):
        row_start = i * 25
        row = image[row_start:row_start + 25]
        line = ['#' if p == 1 else ' ' for p in row]
        print(''.join(line))

