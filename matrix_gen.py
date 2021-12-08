import numpy as np
import turtle

camera_dist = 300
screen = turtle.Screen()
screen.tracer(0)
screen.colormode(255)
turtle.bgcolor(55,71,79)
t = turtle.Turtle(visible=False)
t.speed(0)
t.pencolor("white")
cube_pos = (0, 0, 0)
t.pensize(5)

def gettoorigin(coords):
    return ((0 - (coords[0][0] + coords[7][0]) / 2),
            (0 - (coords[0][1] + coords[7][1]) / 2),
            (0 - (coords[0][2] + coords[7][2]) / 2))

def goback(coords):
    return ((coords[0][0] + coords[7][0]) / 2,
            (coords[0][1] + coords[7][1]) / 2,
           (coords[0][2] + coords[7][2]) / 2)

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
    gettoorigins = gettoorigin(coords)
    gobacks = goback(coords)
    for c in coords:
        c[0] += gettoorigins[0]
        c[1] += gettoorigins[1]
        c[2] += gettoorigins[2]
        temp = np.matmul(rotmatrix, c)
        temp[0] += gobacks[0]
        temp[1] += gobacks[1]
        temp[2] += gobacks[2]
        rotated.append(temp)
    return rotated

def rotateX(coords, rad):
    rotmatrix = [[np.cos(rad), 0, -np.sin(rad), 0],
                 [0, 1, 0, 0],
                 [np.sin(rad), 0, np.cos(rad), 0],
                 [0, 0, 0, 1]]
    rotated = []
    gettoorigins = gettoorigin(coords)
    gobacks = goback(coords)
    for c in coords:
        c[0] += gettoorigins[0]
        c[1] += gettoorigins[1]
        c[2] += gettoorigins[2]
        temp = np.matmul(rotmatrix, c)
        temp[0] += gobacks[0]
        temp[1] += gobacks[1]
        temp[2] += gobacks[2]
        rotated.append(temp)
    return rotated


def translate(coords, dx, dy, dz):
    trmatrix = [[1, 0, 0, dx],
                [0, 1, 0, dy],
                [0, 0, 1, dz],
                [0, 0, 0, 1]]
    translated = []
    for c in coords:
        temp = np.matmul(trmatrix, c)
        translated.append(temp)
    return translated

def scale(coords, amnt):
    sclmatrix = [[amnt, 0, 0, 0],
                 [0, amnt, 0, 0],
                 [0, 0, amnt, 0],
                 [0, 0, 0, amnt]]
    scaled = []
    gettoorigins = gettoorigin(coords)
    gobacks = goback(coords)
    for c in coords:
        c[0] += gettoorigins[0]
        c[1] += gettoorigins[1]
        c[2] += gettoorigins[2]
        temp = np.matmul(sclmatrix, c)
        temp[0] += gobacks[0]
        temp[1] += gobacks[1]
        temp[2] += gobacks[2]
        scaled.append(temp)
    return scaled
    
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
    coords = projcoords(coords)
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
    t.clear()
    global vertices
    draw_cube(vertices)

vertices = make_cube()

# ==============================================================================
# translate
def up():
    global vertices
    vertices = translate(vertices, 0, 20, 0)
    animate()

def down():
    global vertices
    vertices = translate(vertices, 0, -20, 0)
    animate()

def left():
    global vertices
    vertices = translate(vertices, -20, 0, 0)
    animate()

def right():
    global vertices
    vertices = translate(vertices, 20, 0, 0)
    animate()

def forward():
    global vertices
    vertices = translate(vertices, 0, 0, 20)
    animate()
    
def backward():
    global vertices
    vertices = translate(vertices, 0, 0, -20)
    animate()
# ==============================================================================

# ==============================================================================
# Rotations 
def rotdown():
    global vertices
    vertices = rotateY(vertices, -0.1)
    animate()

def rotup():
    global vertices
    vertices = rotateY(vertices, 0.1)
    animate()   

def rotleft():
    global vertices
    vertices = rotateX(vertices, -0.1)
    animate()  

def rotright():
    global vertices
    vertices = rotateX(vertices, 0.1)
    animate()  

# ==============================================================================

# ==============================================================================
# Scaling
def scaleup():
    global vertices
    vertices = scale(vertices, 1.1)
    animate()

def scaledown():
    global vertices
    vertices = scale(vertices, 1/(1.1))
    animate()
# ==============================================================================
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(forward, "q")
screen.onkeypress(backward, "e")

screen.onkeypress(rotright, "d")
screen.onkeypress(rotleft, "a")
screen.onkeypress(rotup, "w")
screen.onkeypress(rotdown, "s")

screen.onkeypress(scaleup, "equal")
screen.onkeypress(scaledown, "minus")

draw_cube(vertices)
screen.listen()
turtle.mainloop()