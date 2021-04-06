import arcade
from game.constants import *
from game.hand import Hand

class Player:
    def __init__(self, direction, attacker):
        if direction not in ["left", "right"]:
            raise ValueError("position must be 'left' or 'right'")
        self._a_hand = None
        self._b_hand = None
        self.attacker = attacker
        self.direction = direction
        self._setup(direction)
        self.points = 0
        self.resetting = False
        self.line = None
        
    
    def resetPosition(self):
        self._a_hand.resetPosition(self.attacker)
        self._b_hand.resetPosition(self.attacker)

    def draw(self):
        self._a_hand.draw()
        self._b_hand.draw()
        if(not self.attacker):
            if(self.direction == "left"):
                arcade.draw_line((MAX_X/2), 0, (MAX_X/2), MAX_Y, arcade.color.YELLOW)
                
            elif(self.direction == "right"):
                arcade.draw_line((MAX_X/2), 0, (MAX_X/2), MAX_Y, arcade.color.YELLOW)
        if(self.direction == "right"):
            arcade.draw_text(str(self.points), 0,MAX_Y-20,arcade.color.BLUE)
        elif(self.direction == "left"):
            arcade.draw_text(str(self.points), MAX_X-20,MAX_Y-20,arcade.color.BLUE)
           
            

    def get_a_hand(self):
        return self._a_hand

    def get_b_hand(self):
        return self._b_hand
        
    def displayVictory(self):
        if(self.direction == "right"):
            arcade.draw_text(("Player 1 victory!"), (MAX_X/2),(MAX_Y/2),arcade.color.WHITE)
            arcade.draw_text(str(self.points), 500,600,arcade.color.BLUE)
        if(self.direction == "left"):
            arcade.draw_text(("Player 2 victory!"), (MAX_X/2),(MAX_Y/2),arcade.color.WHITE)
            arcade.draw_text(str(self.points), 600,500,arcade.color.BLUE)

    def update(self):
        self._a_hand.update(self.attacker)
        self._b_hand.update(self.attacker)
        if self.points >= 10:
            self.displayVictory()
    
    def _setup(self, direction):
        if direction == "left":
            self._a_hand = Hand(RIGHT_FACING_A_IMAGE, 1, self.attacker)
            self._a_hand.center_y = A_HAND_Y
            self._b_hand = Hand(RIGHT_FACING_B_IMAGE, 1, self.attacker)
            self._b_hand.center_y = B_HAND_Y
            
        elif direction == "right":
            self._a_hand = Hand(LEFT_FACING_A_IMAGE, -1, self.attacker)
            self._a_hand.center_y = A_HAND_Y
            self._b_hand = Hand(LEFT_FACING_B_IMAGE, -1, self.attacker)
            self._b_hand.center_y = B_HAND_Y
        