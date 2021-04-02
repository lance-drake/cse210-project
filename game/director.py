import arcade
import random

from game import constants
from game.move_player import MovePlayer
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction

from game.enemy import Enemy
from game.director import Director
from game.player import Player
from game.Action import Action

from Maze import main as maze

class Director(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Handsies")

        #entity lists
        self.playersList=None
        self.enemiesList=None

        #player
        self.my_player=None

    def setup(self):
        self.playersList=arcade.SpriteList()
        self.enemiesList=arcade.SpriteList()

        self.my_player=Player()
        self.playersList.append(self.my_player)

        for i in range(constants. ENEMY_COUNT):
            enemy=Enemy()
            self.enemiesList.append(enemy)

    def on_draw(self):
        arcade.start_render()
        self.playersList.draw()
        self.enemiesList.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.my_player.change_y = PLAYER_MOVE_SCALE
        elif key == arcade.key.DOWN:
            self.my_player.change_y = -PLAYER_MOVE_SCALE
        elif key == arcade.key.LEFT:
            self.my_player.change_x = -PLAYER_MOVE_SCALE
        elif key == arcade.key.RIGHT:
            self.my_player.change_x = PLAYER_MOVE_SCALE

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.my_player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.my_player.change_x = 0

    def update(self, delta_time):
        """Movement and Logic"""

        # Update Enemies
        self.enemiesList.update()

        # Hits Enemy
        enemy_hitList=arcade.check_for_collision(self.enemiesList, self.playersList)

        for enemy in enemy_hitList:
            # CALL HANDSIE GAME HERE
            """
            if won game:
                enemy.kill()
            else:
                player.kill()

            """
            


        

