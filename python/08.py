import numpy as np

if __name__ == "__main__":
    lines = open("08.dat", "r").readlines()
    pixels_chars = list(lines[0])
    pixels = list(map(int, pixels_chars))
    width = 25
    height = 6
    image = np.array(pixels, dtype=np.int)
    image = image.reshape((-1, height * width))

    zero_count = np.count_nonzero(image == 0, axis=1)
    min_layer = np.argmin(zero_count)
    layer = image[min_layer]
    one_count = np.count_nonzero(layer == 1)
    two_count = np.count_nonzero(layer == 2)
    print(one_count * two_count)

    image = image.reshape((-1, height,  width))

    depth = image.shape[0]

    final_image = np.full((height, width), 2)
    for z in range(depth):
        layer = image[z]
        for y in range(height):
            for x in range(width):
                if final_image[y][x] == 2:
                    final_image[y][x] = image[z][y][x]
    print(final_image)
