import arcade
import platform

if platform.system() == "Windows":
    STARS_IMAGE_PATH = r"images\stars.jpg"


elif platform.system() == "Linux":
    STARS_IMAGE_PATH = "images/stars.jpg"


TEX_RED_BUTTON_NORMAL = arcade.load_texture(":resources:gui_basic_assets/button/red_normal.png")
TEX_RED_BUTTON_HOVER = arcade.load_texture(":resources:gui_basic_assets/button/red_hover.png")
TEX_RED_BUTTON_PRESS = arcade.load_texture(":resources:gui_basic_assets/button/red_press.png")


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Python Z-Type Clone"

WORD_BANK = ["Python", "ARCADE", "CODING", "GAMEDEV", "COMPUTER", "ALGORITHM", "CYBER"]





