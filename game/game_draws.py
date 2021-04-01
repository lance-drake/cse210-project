from game.action import Action
from game import constants

import arcade

class gameDraw(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        for player in cast["player"]:
            player.draw()
        for enemy in cast["enemy"]:
            enemy.draw()