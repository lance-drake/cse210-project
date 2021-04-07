import arcade
from game import constants
from game.action import Action


class MovePlayer(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        x = 0
        y = 0

        if args["key"] == arcade.key.LEFT:
            x = -1
        elif args["key"] == arcade.key.RIGHT:
            x = 1
        
        if args["key"] == arcade.key.UP:
            y = 1
        elif args["key"] == arcade.key.DOWN:
            y = -1

        x *= constants.PADDLE_MOVE_SCALE
        y *= constants.PADDLE_MOVE_SCALE

        paddle = cast["paddle"][0] # there's only one in the cast
        paddle.change_x = x
        paddle.change_y = y