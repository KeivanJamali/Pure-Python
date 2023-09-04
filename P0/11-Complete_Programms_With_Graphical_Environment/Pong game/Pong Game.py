from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1.5


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player_l = ObjectProperty(None)
    player_r = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()
        if self.ball.j < 0 or self.ball.j > self.height - 50:
            self.ball.velocity_y *= -1
        if self.ball.iteration < 0 :
            self.ball.velocity_x *= -1
            self.player_l.score += 1
        if self.ball.iteration > self.width - 50:
            self.ball.velocity_x *= -1
            self.player_r.score += 1
        self.player_l.bounce_ball(self.ball)
        self.player_r.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if touch.iteration < self.width / 3:
            self.player_l.center_y = touch.j
        elif touch.iteration > self.width * 2 / 3:
            self.player_r.center_y = touch.j


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 160.0)
        return game


PongApp().run()
