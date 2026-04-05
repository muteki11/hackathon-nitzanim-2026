import arcade
from Game_Win import GameView

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
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.buttons = [
            TextButton(400, 350, 200, 50, "PLAY", arcade.color.GO_GREEN, self.start_game),
            TextButton(400, 280, 200, 50, "SETTINGS", arcade.color.GRAY, self.open_settings),
            TextButton(400, 210, 200, 50, "EXIT", arcade.color.MAROON, arcade.exit)
        ]

    def on_draw(self):
        self.clear()
        arcade.draw_text("Stars", 400, 500, arcade.color.WHITE, 40, anchor_x="center")
        for b in self.buttons:
            b.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        for b in self.buttons:
            if b.is_clicked(x, y):
                b.action()

    def start_game(self):
        game_view = GameView()
        self.window.show_view(game_view)

    def open_settings(self):
        pass
