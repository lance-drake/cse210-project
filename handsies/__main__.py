import arcade

from game import constants
from game.director import Director
from game.player import Player
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.key_release_action import KeyReleaseActon
from game.move_actors_action import MoveActorsAction



def main():

    # create the cast {key: tag, value: list}
    cast = {}
    cast["players"] = []
    cast["players"].append(Player("left", True))
    cast["players"].append(Player("right", False))
     
    # create the script {key: tag, value: list}
    script = {}
    control_actors_action = ControlActorsAction()
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    key_release_action = KeyReleaseActon()
    draw_actors_action = DrawActorsAction()
    script[Director.ON_KEY_PRESS] = [control_actors_action]
    script[Director.ON_KEY_RELEASE] = [key_release_action]
    script[Director.ON_UPDATE] = [move_actors_action, handle_collisions_action]
    script[Director.ON_DRAW] = [draw_actors_action]

    # start the game
    director = Director(constants.MAX_X, constants.MAX_Y)
    director.direct_scene(cast, script)
    arcade.run()


if __name__ == "__main__":
    main()