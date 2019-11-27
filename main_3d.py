from random import random

def init_matrix(x_max, y_max, z_max, p):
    matrix = []
    for x in range(x_max):
        column = []
        for y in range(y_max):
            row = []
            for z in range(z_max):
                r = random()
                row.append(1 if r < p else 0)
            column.append(row)
        matrix.append(column)
    return matrix

def update_matrix_3D(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            for z in range(len(matrix[x][y])):
                neighbour_count = 0
                for dx, dy, dz in range(-1,2), range(-1, 2), range(-1, 2):
                    if (dx == dy == dz == 0):
                        continue
                    if (x+dx >= len(matrix)) or (x+dx < 0):
                        continue
                    if (y+dy >= len(matrix[x])) or (y+dy < 0):
                        continue
                    if (z+dz >= len(matrix[x][y])) or (z+dz < 0):
                        continue
                    if matrix[x+dx][y+dy][z+dz] == 1:
                        neighbour_count += 1
                if neighbour_count == 3:
                    matrix[x][y][z] = 1
                elif neighbour_count > 4 or neighbour_count < 2:
                    matrix[x][y][z] = 0