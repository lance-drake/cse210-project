from game import constants
from game.action import Action
from game.AudioStreamButton import AudioStreamButton
class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        player1 = cast["players"][0]
        player2 = cast["players"][1]
        audio = AudioStreamButton(constants.SLAP_AUDIO, 1, 0.5)

        if player1.get_a_hand().collides_with_sprite(player2.get_a_hand()):
            if(player1.attacker):
                player1.points += 1
                if player1.points >= 10:
                    player1.displayVictory()
            elif(player2.attacker):
                player2.points += 1
                if player2.points >= 10:
                    player2.displayVictory()
            audio.play()
            player1.resetPosition()
            player2.resetPosition()
        if player1.get_b_hand().collides_with_sprite(player2.get_b_hand()):
            if(player1.attacker):
                player1.points += 1
            elif(player2.attacker):
                player2.points += 1
            audio.play()
            player1.resetPosition()
            player2.resetPosition()

        if(player1.attacker):
            if(player2.get_a_hand().passedLine and player1.get_a_hand()._key_down):
                self.switchAttacker(cast)
            if(player2.get_b_hand().passedLine and player1.get_b_hand()._key_down):
                self.switchAttacker(cast)

        elif(player2.attacker):
            if(player1.get_a_hand().passedLine and player2.get_a_hand()._key_down):
                self.switchAttacker(cast)
            if(player1.get_b_hand().passedLine and player2.get_b_hand()._key_down):
                self.switchAttacker(cast)

    def switchAttacker(self, cast):
        player1 = cast["players"][0]
        player2 = cast["players"][1]

        player1.attacker = not player1.attacker
        player2.attacker = not player2.attacker
        player1.resetPosition()
        player2.resetPosition()