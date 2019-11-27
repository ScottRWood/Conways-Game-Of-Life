from random import random
import matplotlib.pyplot as plt
from matplotlib import colors

def init_matrix(x_max, y_max, p):
    matrix = []
    for y in range(y_max):
        row = []
        for x in range(x_max):
            r = random()
            row.append(1 if r < p else 0)
        matrix.append(row)
    return matrix


def update_matrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            neighbour_count = 0
            for dy in range(-1,2):
                for dx in range(-1,2):
                    if (dx == 0 and dy == 0) or (x+dx > len(matrix[y]) - 1) or (x+dx < 0) or (y+dy > len(matrix) - 1) or (y+dy < 0):
                        continue
                    if matrix[y+dy][x+dx] == 1:
                        neighbour_count += 1
            if neighbour_count == 3:
                matrix[y][x] = 1
            elif neighbour_count > 4 or neighbour_count < 2:
                matrix[y][x] = 0

if __name__ == "__main__":
    x_max = 100
    y_max = 100
    p = 0.5

    matrix = init_matrix(x_max, y_max, p)
    print(matrix)
    while True:
        cmap = colors.ListedColormap(['green', 'white'])
        bounds = [0,0.5,1]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(matrix, cmap=cmap, norm=norm)

        plt.show()
        plt.close()

        update_matrix(matrix)