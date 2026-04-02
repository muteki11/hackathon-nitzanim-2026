import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Python Z-Type Clone"

WORD_BANK = ["Python", "ARCADE", "CODING", "GAMEDEV", "COMPUTER", "ALGORITHM", "CYBER"]


class ZTypeGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.enemies = []
        self.active_enemy = None
        self.score = 0
        self.spawn_timer = 0

        self.score_text = arcade.Text(f"Score: {self.score}", 10, 20, arcade.color.GREEN, 14)

    def spawn_word(self):
        word_text = random.choice(WORD_BANK)
        x_pos = random.randint(100, SCREEN_WIDTH - 100)

        # Create a Text object for better performance
        text_obj = arcade.Text(word_text, x_pos, SCREEN_HEIGHT, arcade.color.WHITE, 18, anchor_x="center")

        enemy = {
            "full_word": word_text,
            "remaining": word_text,
            "text_obj": text_obj
        }
        self.enemies.append(enemy)

    def on_update(self, delta_time):
        self.spawn_timer += delta_time
        if self.spawn_timer > 2.0:
            self.spawn_word()
            self.spawn_timer = 0

        for enemy in self.enemies[:]:
            enemy["text_obj"].y -= 1

            if enemy["text_obj"].y < 0:
                self.enemies.remove(enemy)
                self.score -= 5
                self.update_score_display()

    def update_score_display(self):
        self.score_text.text = f"Score: {self.score}"

    def on_draw(self):
        self.clear()  # Replaced start_render()

        for enemy in self.enemies:
            if enemy == self.active_enemy:
                enemy["text_obj"].color = arcade.color.YELLOW
            else:
                enemy["text_obj"].color = arcade.color.WHITE

            enemy["text_obj"].draw()

        self.score_text.draw()

    def on_key_press(self, key, modifiers):
        try:
            char = chr(key)
        except ValueError:
            return

        if self.active_enemy:
            if self.active_enemy["remaining"].startswith(char):
                self.active_enemy["remaining"] = self.active_enemy["remaining"][1:]
                # Update the displayed text object
                self.active_enemy["text_obj"].text = self.active_enemy["remaining"]

                if len(self.active_enemy["remaining"]) == 0:
                    self.enemies.remove(self.active_enemy)
                    self.active_enemy = None
                    self.score += 10
                    self.update_score_display()
        else:
            for enemy in self.enemies:
                if enemy["remaining"].startswith(char):
                    self.active_enemy = enemy
                    self.active_enemy["remaining"] = self.active_enemy["remaining"][1:]
                    self.active_enemy["text_obj"].text = self.active_enemy["remaining"]
                    break


if __name__ == "__main__":
    game = ZTypeGame()
    arcade.run()