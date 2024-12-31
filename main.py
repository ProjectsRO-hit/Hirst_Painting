from turtle import Screen
import turtle as t
import random as rd

color_list = [
    (229, 228, 226), (225, 223, 224), (199, 176, 117), (124, 37, 24),
    (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54),
    (220, 224, 228), (108, 68, 84), (113, 161, 175), (40, 37, 35),
    (23, 122, 173), (64, 153, 139), (77, 40, 48), (90, 142, 53),
    (9, 67, 47), (180, 97, 80), (131, 39, 41), (211, 202, 152),
    (140, 172, 157), (176, 152, 158), (178, 201, 186), (218, 181, 171),
    (169, 200, 209), (205, 183, 188), (41, 75, 61), (148, 116, 122),
    (39, 72, 81), (97, 138, 153)
]

def draw_row():
    """Draws a single row of 10 dots."""
    for _ in range(10):  # Change from 11 to 10
        tim.dot(20, rd.choice(color_list))
        tim.penup()
        tim.forward(50)

def move_up():
    """Moves the turtle up to the next row."""
    tim.penup()
    tim.backward(500)  # Move back to the start of the row
    tim.left(90)
    tim.forward(50)  # Move up to the next row
    tim.right(90)

# Setup Turtle
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()

# Set starting position
tim.penup()
tim.goto(-250, -250)  # Center the grid
tim.pendown()

# Draw 10 rows of dots
for _ in range(10):  # Draw 10 rows
    draw_row()
    move_up()

# Exit on click
screen = Screen()
screen.exitonclick()
