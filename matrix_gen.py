import numpy as np
import turtle
import time

camera_dist = 300
screen = turtle.Screen()
screen.tracer(0)
t = turtle.Turtle(visible=False)
t.speed(0)

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
    
def rotateY(coords, rad):
    rotmatrix = [[1, 0, 0, 0],                 
                 [0, np.cos(rad), -np.sin(rad), 0],
                 [0, np.sin(rad), np.cos(rad), 0],
                 [0, 0, 0, 1]]
    rotated = []
    for c in coords:
        temp = np.matmul(rotmatrix, c)
        rotated.append(temp)
    return rotated

def rotateX(coords, rad):
    rotmatrix = [[np.cos(rad), 0, -np.sin(rad), 0],
                 [0, 1, 0, 0],
                 [np.sin(rad), 0, np.cos(rad), 0],
                 [0, 0, 0, 1]]
    rotated = []
    for c in coords:
        temp = np.matmul(rotmatrix, c)
        rotated.append(temp)
    return rotated


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
    return vertices

def draw_cube(coords):
    t.penup()
    # draw the vertices
    # for c in coords:
    #     t.goto(c[0], c[1])
    #     t.dot(20)
    
    # draw the edges in a certain order
    # front square
    t.goto(coords[0][0], coords[0][1])
    t.pendown()
    t.goto(coords[3][0], coords[3][1])
    t.goto(coords[6][0], coords[6][1])
    t.goto(coords[2][0], coords[2][1])
    t.goto(coords[0][0], coords[0][1])
    # back square
    t.goto(coords[1][0], coords[1][1])
    t.goto(coords[5][0], coords[5][1])
    t.goto(coords[7][0], coords[7][1])
    t.goto(coords[4][0], coords[4][1])
    t.goto(coords[1][0], coords[1][1])
    t.penup()
    t.goto(coords[2][0], coords[2][1])
    t.pendown()
    t.goto(coords[4][0], coords[4][1])
    t.penup()
    t.goto(coords[3][0], coords[3][1])
    t.pendown()
    t.goto(coords[5][0], coords[5][1])
    t.penup()
    t.goto(coords[6][0], coords[6][1])
    t.pendown()
    t.goto(coords[7][0], coords[7][1])

    turtle.update()

def animate():
    vertices = make_cube()
    global camera_dist
    while(True):
        vertices = rotateX(vertices, 0.01)
        vertices = rotateY(vertices, 0.01)
        draw_cube(projcoords(vertices))
        time.sleep(0.05)
        t.clear()

animate()
