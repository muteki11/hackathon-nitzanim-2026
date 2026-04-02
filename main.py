import arcade
from arcade.color import BLUEBONNET, REDWOOD, GREEN
from constants import *
from topic_choice import Topic_choice

def main():
    #NOTE: RIGHT NOW GAME IS TOPIC_CHOICE BUT OSHRI NEEDS TO CHANGE SOME STUFF AND THEN IT WOULD BE THE MENU. 

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game = Topic_choice()
    game.setup()
    window.show_view(game)
    arcade.run()

main()













if __name__ == "__main__":
    main()

