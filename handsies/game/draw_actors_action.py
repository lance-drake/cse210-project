from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        for player in cast["players"]:
            player.draw() 