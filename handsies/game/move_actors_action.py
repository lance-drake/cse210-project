from game.action import Action


class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        players = cast["players"]
        for player in players:
            player.update()