import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Setting up perspective and initial position
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Function to draw axes
def draw_axes():
    glBegin(GL_LINES)

    # X axis in red
    glColor3f(1.0, 0.0, 0.0)
    glVertex3fv((0, 0, 0))
    glVertex3fv((10, 0, 0))

    # Y axis in green
    glColor3f(0.0, 1.0, 0.0)
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 10, 0))

    # Z axis in blue
    glColor3f(0.0, 0.0, 1.0)
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 0, 10))

    glEnd()

# Function to draw points
def draw_points():
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)  # White color for points

    # Replace this with your data points
    points = np.random.rand(1000, 3) * 10  # Example points
    for p in points:
        glVertex3fv(p)

    glEnd()

# Function to handle mouse motion for rotation
def mouse_motion(x, y, last_x, last_y):
    dx, dy = x - last_x, y - last_y
    sensitivity = 0.2
    return dx * sensitivity, dy * sensitivity

# Main loop
def main():
    last_x, last_y = 400, 300
    rotation_x, rotation_y = 0, 0
    pygame.mouse.set_pos([last_x, last_y])
    pygame.event.get()  # Clear event queue

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        x, y = pygame.mouse.get_pos()
        dx, dy = mouse_motion(x, y, last_x, last_y)
        rotation_x += dy
        rotation_y += dx

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0, 0, 0, 0, 0, 1, 0, 1, 0)
        glTranslatef(0.0, 0.0, -5)
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)

        draw_axes()
        draw_points()
        pygame.display.flip()
        pygame.time.wait(10)

        last_x, last_y = x, y

main()
