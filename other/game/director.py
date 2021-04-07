import arcade
import random
import constants
from enemy import Enemy
from player import Player
#from Maze import main as maze

class Director(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, "Handsies")

        #entity lists
        self.playersList=None
        self.enemiesList=None
        arcade.set_background_color(arcade.color.AMAZON)

        #player
        self.my_player=None

    def setup(self):
        #create list for sprites
        self.playersList=arcade.SpriteList()
        self.enemiesList=arcade.SpriteList()

        #create player
        self.my_player=Player(":resources:images/enemies/fishPink.png")
        self.playersList.append(self.my_player)
        self.my_player.center_x = 10
        self.my_player.center_y = 10

        #create enemies
        for i in range(constants. ENEMY_COUNT):
            enemy=Enemy(":resources:images/enemies/frog.png")
            self.enemiesList.append(enemy)

    def on_draw(self):
        arcade.start_render()
        self.playersList.draw()
        self.enemiesList.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.my_player.change_y = constants.PLAYER_MOVE_SCALE
        elif key == arcade.key.DOWN:
            self.my_player.change_y = -constants.PLAYER_MOVE_SCALE
        elif key == arcade.key.LEFT:
            self.my_player.change_x = -constants.PLAYER_MOVE_SCALE
        elif key == arcade.key.RIGHT:
            self.my_player.change_x = constants.PLAYER_MOVE_SCALE

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.my_player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.my_player.change_x = 0

    def update(self, delta_time):
        """Movement and Logic"""

        # Update Players
        self.playersList.update()

        # Update Enemies
        self.enemiesList.update()

        # Hits Enemy
        enemy_hitList=arcade.check_for_collision_with_list(self.enemiesList[0], self.playersList)

        for enemy in enemy_hitList:
            # CALL HANDSIE GAME HERE
            """
            if won game:
                enemy.kill()
            else:
                player.kill()

            """
            print('cat')

