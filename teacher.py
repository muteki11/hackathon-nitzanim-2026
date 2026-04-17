import arcade.gui
from arcade.gui import UITextureButton
from unicodedata import category
from constants import *

class Teacher(arcade.View):
    def __init__(self):
        super().__init__()

        self.question_clicked = False

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        #self.input_text = ""

        self.input_field = arcade.gui.UIInputText(
            x=300, y=250, width=200, height=40,
            text='',
            text_color=arcade.color.WHITE
        )
        self.input_box = self.input_field.with_border(width=2, color=arcade.color.GRAY)
        self.manager.add(self.input_box)


        submit_button = UITextureButton(
            text="add question",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        submit_button.center_x = 400
        submit_button.center_y = 350
        submit_button.on_click = self.submit_question
        self.manager.add(submit_button)



    def update(self, delta_time):
        if self.question_clicked:
            arcade.draw_text("question added", 400, 400, arcade.color.WHITE, 20, anchor_x="center",
                             font_name="algerian")

    def submit_question(self, event):
        self.question_clicked = True
        arcade.draw_text("question added", 400, 400, arcade.color.WHITE, 20, anchor_x="center", font_name="algerian")
       # if len(self.input_field.text) > 0:
       #     arcade.draw_text("question added", 400, 400, arcade.color.WHITE, 20, anchor_x="center", font_name="algerian")
       # else:
       #     arcade.draw_text("invalid question!", 400, 400, arcade.color.WHITE, 20, anchor_x="center", font_name="algerian")

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):
        self.clear()
        arcade.draw_text("Teacher settings", 400, 500, arcade.color.WHITE, 40, anchor_x="center", font_name="algerian")
        self.manager.draw()

    '''def setup(self,score,lives,category_bank):
        self.score = score
        self.lives = lives
        self.category_bank = category_bank
    


    def change_to_menu(self, event):
        from Menu_Win import MenuView
        game = MenuView()
        game.setup()
        self.window.show_view(game)

    def change_to_topics(self,event):
        from topic_choice import Topic_choice
        game = Topic_choice()
        game.setup()
        self.window.show_view(game)

    def change_to_game(self,event):
        from Game_Win import GameView
        game = GameView()
        game.setup(self.category_bank)
        self.window.show_view(game)
'''

