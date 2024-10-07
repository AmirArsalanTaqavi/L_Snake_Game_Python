from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    pass


class Food:
    pass


def next_turn():
    pass


def change_direction(new_direction):
    pass


def check_collision():
    pass


def game_over():
    pass


windows = Tk()
windows.title("Snake Game")
windows.resizable(False, False)

score = 0
direction = "down"

label = Label(windows, text="Score: {}".format(score), font=("Consolas", 40))
label.pack()

canvas = Canvas(windows, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

windows_width = window.winfo_width()
windows_height = window.winfo_height()
screen_width = window.winfo_width()
screen_width = window.winfo_screenheight()

windows.mainloop()
