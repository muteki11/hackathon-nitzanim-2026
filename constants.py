import arcade
import platform

if platform.system() == "Windows":
    STARS_IMAGE_PATH = r"images\stars.jpg"
    Menu_Background = r"images\MenuBackground.jpg"


elif platform.system() == "Linux":
    STARS_IMAGE_PATH = "images/stars.jpg"
    Menu_Background = "images\MenuBackground.jpg"



TEX_RED_BUTTON_NORMAL = arcade.load_texture(":resources:gui_basic_assets/button/red_normal.png")
TEX_RED_BUTTON_HOVER = arcade.load_texture(":resources:gui_basic_assets/button/red_hover.png")
TEX_RED_BUTTON_PRESS = arcade.load_texture(":resources:gui_basic_assets/button/red_press.png")

#NOTE: screen constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bagrut Type"

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

PHYSICS_BANK = [
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


MATH_BANK = [
    # ── MATH ──────────────────────────────────────────────────────────────────
    {"q": "What is 7 times 8?",                                              "a": "56",            "cat": "Math"},
    {"q": "What is the square root of 144?",                                 "a": "12",            "cat": "Math"},
    {"q": "What is 15 percent of 200?",                                      "a": "30",            "cat": "Math"},
    {"q": "How many degrees are in a triangle?",                             "a": "180",           "cat": "Math"},
    {"q": "How many degrees are in a full circle?",                          "a": "360",           "cat": "Math"},
    {"q": "What is the value of pi rounded to 2 decimal places?",           "a": "3.14",          "cat": "Math"},
    {"q": "What is 12 squared?",                                             "a": "144",           "cat": "Math"},
]

HISTORY_BANK = [
    {"q": "In what year did World War II end?",                              "a": "1945",          "cat": "History"},
    {"q": "In what year did World War I begin?",                             "a": "1914",          "cat": "History"},
    {"q": "Who was the first man to walk on the Moon?",                      "a": "neil armstrong","cat": "History"},
    {"q": "In what year did the Berlin Wall fall?",                          "a": "1989",          "cat": "History"},
    {"q": "What country dropped the atomic bomb on Hiroshima?",              "a": "usa",           "cat": "History"},
    {"q": "Who was the leader of Nazi Germany?",                             "a": "hitler",        "cat": "History"},
    {"q": "What was the name of the ship that sank in 1912?",                "a": "titanic",       "cat": "History"},
    {"q": "What year did the French Revolution begin?",                      "a": "1789",          "cat": "History"},
    {"q": "Who invented the telephone?",                                     "a": "bell",          "cat": "History"},
    {"q": "Who invented the light bulb?",                                    "a": "edison",        "cat": "History"},
    {"q": "What empire built the Colosseum?",                                "a": "roman",         "cat": "History"},
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





