
import arcade
from arcade.gui import UITextureButton
from topic_choice import Topic_choice
from constants import *


class TextButton:
    def __init__(self, x, y, width, height, text, color, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.action = action

    def draw(self):
        arcade.draw_lrbt_rectangle_filled(
            self.x - self.width / 2,
            self.x + self.width / 2,
            self.y - self.height / 2,
            self.y + self.height / 2,
            self.color
        )
        arcade.draw_text(self.text, self.x, self.y, arcade.color.WHITE, 14, anchor_x="center", anchor_y="center")

    def is_clicked(self, x, y):
        return (self.x - self.width/2 < x < self.x + self.width/2 and
                self.y - self.height/2 < y < self.y + self.height/2)


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
            text="Settings",
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
        return

    def exit(self, event):
        arcade.exit()
        return