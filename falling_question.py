from constants import *
import random



def _color4(c):
    return (c[0], c[1], c[2], 255) if len(c) == 3 else c

def draw_rect_f(cx, cy, w, h, color):
    arcade.draw_rect_filled(arcade.XYWH(cx, cy, w, h), _color4(color))

def draw_rect_o(cx, cy, w, h, color, border=1):
    arcade.draw_rect_outline(arcade.XYWH(cx, cy, w, h), _color4(color), border)


class FallingQuestion:
    def __init__(self, qa, x, speed):
        self.question = qa["q"]
        self.answer   = qa["a"]
        self.cat      = qa["cat"]
        self.x        = x
        self.y        = PLAY_H + 20.0
        self.speed    = speed
        self.color    = CAT_COLORS.get(self.cat, (80, 220, 255, 255))
        #self.color =  (255,0,0, 0) 
        self.shake    = 0.0

    def update(self, dt):
        self.y -= self.speed * dt
        if self.y < PLAY_H * 0.3 and random.random() < 0.06:
            self.shake = 0.25
        self.shake = max(0.0, self.shake - dt * 4)

    def _wrap(self, text, max_ch=44):
        lines, cur = [], ""
        for word in text.split():
            test = (cur + " " + word).strip()
            if len(test) > max_ch:
                if cur:
                    lines.append(cur)
                cur = word
            else:
                cur = test
        if cur:
            lines.append(cur)
        return lines

    def draw(self, targeted=False):
        sx = self.x + (random.randint(-3, 3) if self.shake > 0 else 0)
        sy = self.y
        r, g, b, _ = self.color

        bw = len(self.cat) * 7 + 14
        draw_rect_f(sx, sy + 30, bw, 18, (r, g, b, 70))
        draw_rect_o(sx, sy + 30, bw, 18, (r, g, b, 160), 1)
        

        arcade.draw_text(self.cat, sx, sy + 30,
                         (r, g, b, 220), font_size=9, bold=True,
                         anchor_x="center", anchor_y="center")

        lines = self._wrap(self.question)
        qcol  = (255, 230, 60, 255) if targeted else (180, 220, 255, 255)
        for i, line in enumerate(lines):
            arcade.draw_text(line, sx, sy - i * 17,
                             qcol, font_size=12, bold=targeted,
                             anchor_x="center", anchor_y="top")

        if targeted:
            arcade.draw_line(sx, sy - len(lines) * 17, sx, INPUT_BAR_H,
                             (r, g, b, 50), 1)

    @property
    def reached_bottom(self):
        return self.y < INPUT_BAR_H + 12

