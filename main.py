import arcade
from arcade.color import BLUEBONNET, REDWOOD, GREEN
from constants import *
from Menu_Win import MenuView


def main():
    #NOTE: RIGHT NOW GAME IS TOPIC_CHOICE BUT IT WILL BE THE MENU ONCE CREATED 

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game = MenuView()
    game.setup()
    window.show_view(game)
    arcade.run()



main()













if __name__ == "__main__":
    main()

