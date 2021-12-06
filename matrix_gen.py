import numpy as np
import turtle

camera_dist = 1000

def projcoords(coords):
    projmatrix = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, (-1 / camera_dist), 1]]
    projected = []
    for c in coords:
        temp = np.matmul(projmatrix, c)
        temp = np.divide(temp, 1 - (c[2] / camera_dist))
        projected.append(temp)
    return projected
    

def make_cube():
    length = 100
    vertices = [
                [-length, -length, -length, 1],
                [length, -length, -length, 1],
                [-length, length, -length, 1],
                [-length, -length, length, 1],
                [length, length, -length, 1],
                [length, -length, length, 1],
                [-length, length, length, 1],
                [length, length, length, 1]
    ]
    for v in vertices:
        v = np.transpose(v)
    vertices = projcoords(vertices)
    draw_cube(vertices)

def draw_cube(coords):
    t = turtle.Turtle()
    t.penup()
    for c in coords:
        t.goto(c[0], c[1])
        t.dot(20)
    while (True):
        continue

make_cube()
