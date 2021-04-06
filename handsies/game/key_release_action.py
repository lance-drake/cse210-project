import arcade
from game import constants
from game.action import Action


class KeyReleaseActon(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        player1 = cast["players"][0]
        player2 = cast["players"][1]

        if args["key"] == arcade.key.A:
            player1.get_a_hand().stop(player1.attacker)
            
        elif args["key"] == arcade.key.D:
            player1.get_b_hand().stop(player1.attacker)
           
        
        if args["key"] == arcade.key.J:
            player2.get_a_hand().stop(player2.attacker)
            
        elif args["key"] == arcade.key.L:
            player2.get_b_hand().stop(player2.attacker)
            