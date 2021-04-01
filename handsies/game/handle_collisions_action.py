from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        player1 = cast["players"][0]
        player2 = cast["players"][1]
        
        if player1.get_a_hand().collides_with_sprite(player2.get_a_hand()):
            print("player1's a collided with player2's a!")
        
        if player1.get_b_hand().collides_with_sprite(player2.get_b_hand()):
            print("player1's b collided with player2's b!")
        