import arcade
import arcade.gui
from arcade.gui import UITextureButton
from constants import *


class Topic_choice(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        
        #NOTE: BACK BUTTON
        back_button = UITextureButton(
            text="BACK",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        back_button.center_x = 120
        back_button.center_y = 100
        back_button.on_click = self.change_to_menu
        self.manager.add(back_button)
        

        #NOTE: MATH BUTTON  
        math_button = UITextureButton(
            text="MATHEMATICS",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        math_button.center_x = 120
        math_button.center_y = 330
        math_button.on_click = self.change_to_game_math
        self.manager.add(math_button)
        
        #NOTE: PHYSICS BUTTON
        physics_button = UITextureButton(
            text="PHYSICS",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        physics_button.center_x = 400
        physics_button.center_y = 330
        physics_button.on_click = self.change_to_game_physics
        self.manager.add(physics_button)
        
        #NOTE: HISTORY OR PROGRAMMING BUTTON
        his_or_pro_button = UITextureButton(
            text="HISTORY/PROGRAMMING",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        his_or_pro_button.center_x = 680
        his_or_pro_button.center_y = 330
        his_or_pro_button.on_click = self.change_to_game_history_or_programming
        self.manager.add(his_or_pro_button)
 
    
    def setup(self):
        self.background = arcade.load_texture(STARS_IMAGE_PATH)


    def on_draw(self):
        self.clear() 

        arcade.draw_texture_rect(
            texture=self.background, 
            #rect=arcade.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
            rect=arcade.Rect(left=0,bottom=0,right=0,top=0,width=SCREEN_WIDTH,height=SCREEN_HEIGHT,x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
        )
        #arcade.draw_texture_rectangle()

        self.manager.draw()
     


    def change_to_menu(self, event):
        #TODO: change to the main_menu window once possible 
        print("changed to menu")


    def change_to_game_history_or_programming(self, event):
        #TODO: change to the game window once possible 
        print("changed to game history/programming")
    

    def change_to_game_math(self, event):
        #TODO: change to the game window once possible 
        print("changed to game math")
    
    def change_to_game_physics(self, event):
        #TODO: change to the game window once possible 
        print("changed to game physics")



