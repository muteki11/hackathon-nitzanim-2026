
import arcade
from arcade.gui import UITextureButton
from topic_choice import Topic_choice
from constants import *
from teacher import Teacher


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = None
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        play_btn = UITextureButton(
            text="Play",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        play_btn.center_x = 400
        play_btn.center_y = 350
        self.manager.add(play_btn)
        play_btn.on_click = self.change_to_topic

        setting_btn = UITextureButton(
            text="Teacher Settings",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        setting_btn.center_x = 400
        setting_btn.center_y = 280
        self.manager.add(setting_btn)
        setting_btn.on_click = self.change_to_settings

        exit_btn = UITextureButton(
            text="Exit",
            width=200,
            texture=TEX_RED_BUTTON_NORMAL,
            texture_hovered=TEX_RED_BUTTON_HOVER,
            texture_pressed=TEX_RED_BUTTON_PRESS,
        )
        exit_btn.center_x = 400
        exit_btn.center_y = 210
        self.manager.add(exit_btn)
        exit_btn.on_click = self.exit

    def setup(self):
        self.background = arcade.load_texture(Menu_Background)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)


    def on_draw(self):
        self.clear()

        if self.background:
            arcade.draw_texture_rect(self.background, self.window.rect)

        arcade.draw_text("Bagrut Type", 400, 500, arcade.color.WHITE, 40, anchor_x="center",font_name="algerian")

        self.manager.draw()


    def start_game(self):
        from topic_choice import Topic_choice
        topic_choice_view = Topic_choice()
        topic_choice_view.setup() 
        self.window.show_view(topic_choice_view)

    def change_to_topic(self, event):
        game = Topic_choice()
        game.setup()
        self.window.show_view(game)

    def change_to_settings(self, event):
        game = Teacher()
        self.window.show_view(game)

    def exit(self, event):
        arcade.exit()
        return