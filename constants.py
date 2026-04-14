import arcade
import platform

if platform.system() == "Windows":
    STARS_IMAGE_PATH = r"images\stars.jpg"


elif platform.system() == "Linux":
    STARS_IMAGE_PATH = "images/stars.jpg"


TEX_RED_BUTTON_NORMAL = arcade.load_texture(":resources:gui_basic_assets/button/red_normal.png")
TEX_RED_BUTTON_HOVER = arcade.load_texture(":resources:gui_basic_assets/button/red_hover.png")
TEX_RED_BUTTON_PRESS = arcade.load_texture(":resources:gui_basic_assets/button/red_press.png")

#NOTE: screen constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Learning Stars"

#NOTE: input bar height
INPUT_BAR_H = 80
PLAY_H = SCREEN_HEIGHT - INPUT_BAR_H

#NOTE: Game constants
INITIAL_SPEED  = 10
MAX_ACTIVE = 5
SPAWN_INTERVAL = 3.5
MAX_LIVES      = 5
SPEED_PER_LVL  = 3


#NOTE: questions and answers bank

QA_BANK = [
    # ── PHYSICS ───────────────────────────────────────────────────────────────
    {"q": "What force pulls objects toward the ground?",                     "a": "gravity",       "cat": "Physics"},
    {"q": "What is the basic unit of matter?",                               "a": "atom",          "cat": "Physics"},
    {"q": "What type of energy does a moving car have?",                     "a": "kinetic",       "cat": "Physics"},
    {"q": "What do we call stored energy (like a raised book)?",             "a": "potential",     "cat": "Physics"},
    {"q": "What travels from the Sun to Earth as light and heat?",           "a": "radiation",     "cat": "Physics"},
    {"q": "What is the unit used to measure electric current?",              "a": "ampere",        "cat": "Physics"},
    {"q": "What is the unit used to measure force?",                         "a": "newton",        "cat": "Physics"},
    {"q": "What is the unit of energy?",                                     "a": "joule",         "cat": "Physics"},
    {"q": "Sound cannot travel through what?",                               "a": "vacuum",        "cat": "Physics"},
]





#WORD_BANK = ["Python", "ARCADE", "CODING", "GAMEDEV", "COMPUTER", "ALGORITHM", "CYBER"]



CORRECT_CLR   = (50,  255, 120, 255)
WRONG_CLR     = (255,  80,  80, 255)
SCORE_CLR     = (80,  255, 200, 255)
LIFE_CLR      = (255,  80,  80, 255)


BG            = (8, 12, 28, 255)
CAT_COLORS    = {
    "Physics":  (255, 120,  80, 255),
    "Math":     (100, 200, 255, 255),
    "History":  (255, 210,  80, 255),
    "CS":       (120, 255, 160, 255),
}




