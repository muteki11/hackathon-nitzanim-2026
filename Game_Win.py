import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Python Z-Type Clone"

WORD_BANK = ["python", "ARCADE", "CODING", "GAMEDEV", "COMPUTER", "ALGORITHM", "CYBER"]

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.active_enemy = None
        self.score = 0
        self.spawn_timer = 0
        self.score_text = arcade.Text(f"Score: {self.score}", 10, 20, arcade.color.GREEN, 14)

    def spawn_word(self):
        word_text = random.choice(WORD_BANK)
        x_pos = random.randint(100, 700)
        text_obj = arcade.Text(word_text, x_pos, 600, arcade.color.WHITE, 18, anchor_x="center")
        self.enemies.append({"remaining": word_text, "text_obj": text_obj})

    def on_update(self, delta_time):
        self.spawn_timer += delta_time
        if self.spawn_timer > 2.0:
            self.spawn_word()
            self.spawn_timer = 0

        for enemy in self.enemies[:]:
            enemy["text_obj"].y -= 1.5
            if enemy["text_obj"].y < 0:
                self.enemies.remove(enemy)
                self.score -= 5
                self.score_text.text = f"Score: {self.score}"

    def on_draw(self):
        self.clear()

        for enemy in self.enemies:
            if enemy == self.active_enemy:
                enemy["text_obj"].color = arcade.color.RED
            else:
                enemy["text_obj"].color = arcade.color.WHITE
            enemy["text_obj"].draw()

        self.score_text.draw()

    def on_key_press(self, key, modifiers):
        if arcade.key.A <= key <= arcade.key.Z:
            char = chr(key).lower()

            if self.active_enemy:
                if self.active_enemy["remaining"].startswith(char):
                    self.active_enemy["remaining"] = self.active_enemy["remaining"][1:]
                    self.active_enemy["text_obj"].text = self.active_enemy["remaining"]

                    if not self.active_enemy["remaining"]:
                        self.enemies.remove(self.active_enemy)
                        self.active_enemy = None
                        self.score += 10
                        self.score_text.text = f"Score: {self.score}"
            else:
                for enemy in self.enemies:
                    if enemy["remaining"].startswith(char):
                        self.active_enemy = enemy
                        self.active_enemy["remaining"] = self.active_enemy["remaining"][1:]
                        self.active_enemy["text_obj"].text = self.active_enemy["remaining"]
                        break

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game = GameView()
    game.spawn_word()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()
