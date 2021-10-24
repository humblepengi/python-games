"""
space arena python game made using the turtle module
"""

import turtle


class Game(object):
    def __init__(self, width, height, title, bgcolor):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.title = title
        self.bgcolor = bgcolor

    def main(self):
        wn = turtle.Screen()
        wn.setup(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        wn.title(self.title)
        wn.bgcolor(self.bgcolor)
        wn.tracer(0)

        while True:
            wn.update()

game = Game(800, 600, "Space Arena", "black")
game.main()






