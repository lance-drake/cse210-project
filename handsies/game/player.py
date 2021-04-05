import arcade
from game.constants import *
from game.hand import Hand


class Player:
    def __init__(self, direction):
        if direction not in ["left", "right"]:
            raise ValueError("position must be 'left' or 'right'")
        self._a_hand = None
        self._b_hand = None
        self._setup(direction)
        
    def draw(self):
        self._a_hand.draw()
        self._b_hand.draw()

    def get_a_hand(self):
        return self._a_hand

    def get_b_hand(self):
        return self._b_hand
        
    def update(self):
        self._a_hand.update()
        self._b_hand.update()
    
    def _setup(self, direction):
        if direction == "left":
            self._a_hand = Hand(RIGHT_FACING_A_IMAGE,1, 200,0,600)
            self._a_hand.left = 0
            self._a_hand.center_y = A_HAND_Y
            self._b_hand = Hand(RIGHT_FACING_B_IMAGE, -1,200,0,200)
            self._b_hand.left = 200
            self._b_hand.center_y = B_HAND_Y
            
        elif direction == "right":
            self._a_hand = Hand(LEFT_FACING_A_IMAGE, -1, 600,400,900)
            self._a_hand.right = (MAX_X - 200)
            self._a_hand.center_y = A_HAND_Y
            self._b_hand = Hand(LEFT_FACING_B_IMAGE, 1,800,400,800)
            self._b_hand.right = MAX_X
            self._b_hand.center_y = B_HAND_Y
        