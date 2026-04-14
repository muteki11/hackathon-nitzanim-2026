import arcade
import random
from constants import *
from falling_question import FallingQuestion, draw_rect_f
import time

def _color_alpha(c, a):
    return (c[0], c[1], c[2], a)

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.active_enemy = None
        self.score = 0
        self.spawn_timer = 0
        self.score_text = arcade.Text(f"Score: {self.score}", 10, 20, arcade.color.GREEN, 14)

    def setup(self):
        arcade.set_background_color(BG)
        self.state = "menu"
        self.score = 0
        self.lives = MAX_LIVES
        self.level = 1
        self.questions_answered = 0

        self.pool       = QA_BANK.copy()
        random.shuffle(self.pool)
        self.pool_idx   = 0

        self.active_qs   = []
        self.particles   = []
        self.flashes     = []
        self.targeted_q  = None

        self.input_text     = ""
        self.spawn_timer    = 0.0
        self.spawn_interval = SPAWN_INTERVAL
        self.wrong_flash    = 0.0
        self.correct_flash  = 0.0

        self.stars = [
            (random.randint(0, SCREEN_WIDTH),
             random.randint(INPUT_BAR_H, SCREEN_HEIGHT),
             random.random())
            for _ in range(130)
        ]

        #NOTE: spawn 
        
    def _next_qa(self):
        qa = self.pool[self.pool_idx % len(self.pool)]
        self.pool_idx += 1
        if self.pool_idx % len(self.pool) == 0:
            random.shuffle(self.pool)
        return qa

    def _spawn(self):
        if len(self.active_qs) >= MAX_ACTIVE:
            return
        qa       = self._next_qa()
        occupied = [q.x for q in self.active_qs]
        x = random.randint(130, SCREEN_WIDTH - 130)
        for _ in range(25):
            x = random.randint(130, SCREEN_WIDTH - 130)
            if all(abs(x - ox) > 170 for ox in occupied):
                break
        speed = INITIAL_SPEED + (self.level - 1) * SPEED_PER_LVL
        self.active_qs.append(FallingQuestion(qa, x, speed))


    def on_key_press(self, key, mods):
        if self.state in ("menu", "game_over"):
            self.setup()
            self.state = "playing"
            return
        if key == arcade.key.BACKSPACE:
            self.input_text = self.input_text[:-1]
            self._update_target()
        elif key in (arcade.key.ENTER, arcade.key.RETURN):
            self._submit()
        elif key == arcade.key.ESCAPE:
            self.state = "menu"




    def on_text(self, text):
        if self.state != "playing":
            return
        if text.isprintable() and len(self.input_text) < 42:
            self.input_text += text
            self._update_target()

    


    def _update_target(self):
        typed = self.input_text.strip().lower()
        if not typed:
            self.targeted_q = None
            return
        if self.targeted_q and self.targeted_q.answer.startswith(typed):
            return
        candidates = [q for q in self.active_qs if q.answer.startswith(typed)]
        self.targeted_q = min(candidates, key=lambda q: q.y) if candidates else None

    

    def _submit(self):
            typed = self.input_text.strip().lower()
            self.input_text = ""
            if not typed:
                return
            target = self.targeted_q
            if target is None:
                matches = [q for q in self.active_qs if q.answer == typed]
                target  = matches[0] if matches else None
            if target and target.answer == typed:
                self._correct(target)
            else:
                self._wrong()
            self.targeted_q = None


    def _correct(self, q):
        pts = 100 + self.level * 10
        self.score += pts
        self.questions_answered += 1
        self.active_qs.remove(q)



    def _wrong(self):
        self.wrong_flash = 0.4


    



    def on_update(self, dt):
        if self.state != "playing":
            return
        dt = min(dt, 0.05)

        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0.0
            self._spawn()

        for q in self.active_qs[:]:
            q.update(dt)
            if q.reached_bottom:
                self.active_qs.remove(q)
                self.lives -= 1
                self.wrong_flash = 0.6
                if self.lives <= 0:
                    self.state = "game_over"
                    return








    def on_draw(self):
        self.clear()
        if self.state == "playing":
            self._draw_playing()
        #elif self.state == "game_over":
        #    self._draw_game_over()


    def _draw_stars(self):
        for sx, sy, br in self.stars:
            b = int(br * 180 + 55)
            arcade.draw_point(sx, sy, (b, b, min(255, b + 40), 255), 1.5)

    def _draw_grid(self):
        gc = (20, 35, 70, 60)
        for x in range(0, SCREEN_WIDTH, 80):
            arcade.draw_line(x, INPUT_BAR_H, x, SCREEN_HEIGHT, gc, 1)
        for y in range(INPUT_BAR_H, SCREEN_HEIGHT, 60):
            arcade.draw_line(0, y, SCREEN_WIDTH, y, gc, 1)





    def _draw_hud(self):
        arcade.draw_text(f"SCORE  {self.score:,}", 16, SCREEN_HEIGHT - 28,
                         SCORE_CLR, font_size=14, bold=True)
        arcade.draw_text(f"LVL {self.level}", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 28,
                         (200, 200, 255, 255), font_size=14, bold=True,
                         anchor_x="center")
        hearts = "\u2665 " * self.lives + "\u2661 " * (MAX_LIVES - self.lives)
        arcade.draw_text(hearts.strip(), SCREEN_WIDTH - 16, SCREEN_HEIGHT - 28,
                         LIFE_CLR, font_size=14, bold=True, anchor_x="right")
        arcade.draw_line(0, INPUT_BAR_H + 8, SCREEN_WIDTH, INPUT_BAR_H + 8,
                         (255, 60, 60, 100), 2)


    def _draw_input_bar(self):
        draw_rect_f(SCREEN_WIDTH // 2, INPUT_BAR_H // 2, SCREEN_WIDTH, INPUT_BAR_H,
                    (15, 22, 50, 255))
        arcade.draw_line(0, INPUT_BAR_H, SCREEN_WIDTH, INPUT_BAR_H,
                         (60, 100, 180, 255), 2)
        arcade.draw_text("ANSWER:", 16, INPUT_BAR_H // 2,
                         (100, 140, 200, 255), font_size=13, bold=True,
                         anchor_y="center")
        cursor  = "_" if int(time.time() * 2) % 2 == 0 else " "
        t_color = (255, 220, 60, 255) if self.targeted_q else (255, 255, 255, 255)
        arcade.draw_text(self.input_text + cursor, 110, INPUT_BAR_H // 2,
                         t_color, font_size=18, bold=True, anchor_y="center")
        if self.targeted_q:
            hint = self.targeted_q.question
            if len(hint) > 58:
                hint = hint[:58] + "..."
            hint = f"  {self.targeted_q.cat}: {hint}"
            col  = CAT_COLORS.get(self.targeted_q.cat, (160, 160, 160, 255))
            #col = (255,0,0,0) 
            arcade.draw_text(hint, SCREEN_WIDTH - 16, INPUT_BAR_H // 2,
                             _color_alpha(col, 180), font_size=10,
                             anchor_x="right", anchor_y="center")





    def _draw_playing(self):
        self._draw_grid()
        self._draw_stars()
        if self.wrong_flash > 0:
            draw_rect_f(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                        (255, 0, 0, int(self.wrong_flash * 70)))
        if self.correct_flash > 0:
            draw_rect_f(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                        (0, 255, 100, int(self.correct_flash * 55)))
        for p in self.particles:
            p.draw()
        for q in self.active_qs:
            q.draw(targeted=(q is self.targeted_q))
        for f in self.flashes:
            f.draw()
        #self._draw_hud()
        self._draw_input_bar()





'''
if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game = GameView()
    game.setup()
    window.show_view(game) 
    arcade.run()


'''




