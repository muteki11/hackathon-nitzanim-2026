import arcade.gui
from arcade.gui import UITextureButton
from unicodedata import category

from constants import*

class Endgame_win(arcade.View):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 0
        self.category_bank = []

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        play_again_btn = UITextureButton(
            text="Play again",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        play_again_btn.center_x = 400
        play_again_btn.center_y = 350
        play_again_btn.on_click = self.change_to_game
        self.manager.add(play_again_btn)

        back_to_topics = UITextureButton(
            text="Back to menu",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        back_to_topics.center_x = 400
        back_to_topics.center_y = 280
        back_to_topics.on_click = self.change_to_topics
        self.manager.add(back_to_topics)

        back_to_menu_btn = UITextureButton(
            text="Back to Menu",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        back_to_menu_btn.center_x = 400
        back_to_menu_btn.center_y = 210
        back_to_menu_btn.on_click = self.change_to_menu
        self.manager.add(back_to_menu_btn)

    def on_draw(self):
        self.clear()
        arcade.draw_text(f"SCORE  {self.score:,}", 16, SCREEN_HEIGHT - 28,SCORE_CLR, font_size=28, bold=True)
        arcade.draw_text("Game Over", 400, 500, arcade.color.WHITE, 40, anchor_x="center", font_name="algerian")
        self.manager.draw()

    def setup(self,score,lives,category_bank):
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




