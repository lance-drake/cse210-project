import arcade
import Maze.main

class Entity(arcade.Sprite):
    def __init__(self):
        super().__init__('https://arcade.academy/resources/images/enemies/fishPink.png')
        self.center_x = 0
        self.center_y = int(Maze.main.SCREEN_HEIGHT/2)
