import arcade
import random
from constants import *
from falling_question import FallingQuestion, draw_rect_f
import time


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.active_enemy = None
        self.score = 0
        self.spawn_timer = 0
        self.score_text = arcade.Text(f"Score: {self.score}", 10, 20, arcade.color.GREEN, 14)

    def setup(self, category_bank):
        arcade.set_background_color(BG)
        self.state = "playing"
        self.score = 0
        self.lives = MAX_LIVES
        self.level = 1
        self.questions_answered = 0

        self.pool = category_bank.copy()
        random.shuffle(self.pool)
        self.pool_index = 0

        self.active_questions = []
        self.flashes = []
        self.targeted_question = None

        self.input_text = ""
        self.spawn_timer = 0.0
        self.spawn_interval = SPAWN_INTERVAL
        self.wrong_flash_timer = 0.0
        self.correct_flash_timer = 0.0

        self.stars = [
            (random.randint(0, SCREEN_WIDTH),
             random.randint(INPUT_BAR_H, SCREEN_HEIGHT),
             random.random())
            for _ in range(130)
        ]

        #NOTE: spawn 
        
    def _get_next_question(self):
        question_data = self.pool[self.pool_index % len(self.pool)]
        self.pool_index += 1
        if self.pool_index % len(self.pool) == 0:
            random.shuffle(self.pool)
        return question_data

    def _spawn(self):
        if len(self.active_questions) >= MAX_ACTIVE:
            return
        question_data = self._get_next_question()
        occupied_x_positions = [question.x for question in self.active_questions]
        new_x = random.randint(130, SCREEN_WIDTH - 130)
        for _ in range(25):
            new_x = random.randint(130, SCREEN_WIDTH - 130)
            if all(abs(new_x - occupied_x) > 170 for occupied_x in occupied_x_positions):
                break
        speed = INITIAL_SPEED + (self.level - 1) * SPEED_PER_LVL
        self.active_questions.append(FallingQuestion(question_data, new_x, speed))


    def on_key_press(self, key, modifiers):
        if key == arcade.key.BACKSPACE:
            self.input_text = self.input_text[:-1]
            self._update_target()
        elif key in (arcade.key.ENTER, arcade.key.RETURN):
            self._submit()
        elif key == arcade.key.ESCAPE:
            arcade.exit()


    def on_text(self, text):
        if self.state != "playing":
            return
        if text.isprintable() and len(self.input_text) < 42:
            self.input_text += text
            self._update_target()

    


    def _update_target(self):
        typed_text = self.input_text.strip().lower()
        if not typed_text:
            self.targeted_question = None
            return
        if self.targeted_question and self.targeted_question.answer.startswith(typed_text):
            return
        candidates = [q for q in self.active_questions if q.answer.startswith(typed_text)]
        self.targeted_question = min(candidates, key=lambda q: q.y) if candidates else None

    

    def _submit(self):
            typed_text = self.input_text.strip().lower()
            self.input_text = ""
            if not typed_text:
                return
            target = self.targeted_question
            if target is None:
                matches = [q for q in self.active_questions if q.answer == typed_text]
                target = matches[0] if matches else None
            if target and target.answer == typed_text:
                self._handle_correct_answer(target)
            else:
                self._handle_wrong_answer()
            self.targeted_question = None


    def _handle_correct_answer(self, question):
        points = 10
        self.score += points
        self.questions_answered += 1
        self.active_questions.remove(question)
        self.correct_flash_timer = 0.4


    def _handle_wrong_answer(self):
        self.wrong_flash_timer = 0.4




    def on_update(self, delta_time):

        if self.score >= 30:
            arcade.exit()

        delta_time = min(delta_time, 0.05)

        self.spawn_timer += delta_time
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0.0
            self._spawn()

        for question in self.active_questions:
            question.update(delta_time)
            if question.reached_bottom:
                self.active_questions.remove(question)
                self.lives -= 1
                self.wrong_flash_timer = 0.6
                if self.lives <= 0:
                    #TODO: change to game over screen
                    arcade.exit()
                    return

        for flash in self.flashes:
            flash.update(delta_time)

        self.wrong_flash_timer = max(0.0, self.wrong_flash_timer - delta_time)
        self.correct_flash_timer = max(0.0, self.correct_flash_timer - delta_time)





    def on_draw(self):
        self.clear()
        if self.state == "playing":
            self._draw_playing()



    def _draw_stars(self):
        for star_x, star_y, brightness_ratio in self.stars:
            color_value = int(brightness_ratio * 180 + 55)
            arcade.draw_point(star_x, star_y, (color_value, color_value, min(255, color_value + 40), 255), 1.5)

    def _draw_grid(self):
        grid_color = (20, 35, 70, 60)
        for x in range(0, SCREEN_WIDTH, 80):
            arcade.draw_line(x, INPUT_BAR_H, x, SCREEN_HEIGHT, grid_color, 1)
        for y in range(INPUT_BAR_H, SCREEN_HEIGHT, 60):
            arcade.draw_line(0, y, SCREEN_WIDTH, y, grid_color, 1)





    def _draw_hud(self):
        arcade.draw_text(f"SCORE  {self.score:,}", 16, SCREEN_HEIGHT - 28,
                         SCORE_CLR, font_size=14, bold=True)
        

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
        cursor = "_" if int(time.time() * 2) % 2 == 0 else " "
        text_color = (255, 220, 60, 255) if self.targeted_question else (255, 255, 255, 255)
        arcade.draw_text(self.input_text + cursor, 110, INPUT_BAR_H // 2,
                         text_color, font_size=18, bold=True, anchor_y="center")
        
            



    def _draw_playing(self):
        self._draw_grid()
        self._draw_stars()
        if self.wrong_flash_timer > 0:
            draw_rect_f(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                        (255, 0, 0, int(self.wrong_flash_timer * 70)))
        if self.correct_flash_timer > 0:
            draw_rect_f(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                        (0, 255, 100, int(self.correct_flash_timer * 55)))


        for question in self.active_questions:
            question.draw(targeted=(question is self.targeted_question))
        for flash in self.flashes:
            flash.draw()
        
        self._draw_hud()
        self._draw_input_bar()




