import arcade
import arcade.gui
from constants import *

class Topic_choice(arcade.View):
    def __init__(self):
        super().__init__()
        #arcade.set_background_color(arcade.color.BLACK)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        math_button = arcade.gui.UIFlatButton(text="Mathematics", width=200, height=60)
        math_button.center_x = 120
        math_button.center_y = 330
        math_button.on_click = self.change_to_game_math
        self.manager.add(math_button)
    


    
    def setup(self):
        pass

    def on_draw(self):
        self.manager.draw()
    

    def change_to_game_math(self, event):
        print("changed to game math")


