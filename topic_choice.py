import arcade
import arcade.gui
from constants import *

class Topic_choice(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        #NOTE: MATH BUTTON  
        math_button = arcade.gui.UIFlatButton(text="Mathematics", width=200, height=60)
        math_button.center_x = 120
        math_button.center_y = 330
        math_button.on_click = self.change_to_game_math
        self.manager.add(math_button)
        
        #NOTE: PHYSICS BUTTON
        physics_button = arcade.gui.UIFlatButton(text="Physics", width=200, height=60)
        physics_button.center_x = 400
        physics_button.center_y = 330
        physics_button.on_click = self.change_to_game_physics
        self.manager.add(physics_button)
        
        #NOTE: HISTORY OR PROGRAMMING BUTTON
        his_or_pro_button = arcade.gui.UIFlatButton(text="History/Programming", width=200, height=60)
        his_or_pro_button.center_x = 680
        his_or_pro_button.center_y = 330
        his_or_pro_button.on_click = self.change_to_game_history_or_programming
        self.manager.add(his_or_pro_button)
 
    
    def setup(self):
        pass

    def on_draw(self):
        self.manager.draw()
     

    def change_to_game_history_or_programming(self, event):
        #TODO: change to the game window once possible 
        print("changed to game history/programming")
    

    def change_to_game_math(self, event):
        #TODO: change to the game window once possible 
        print("changed to game math")
    
    def change_to_game_physics(self, event):
        #TODO: change to the game window once possible 
        print("changed to game physics")



