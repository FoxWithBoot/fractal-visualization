import turtle
from random import randint


class LSystem2D:
    def __init__(self, axiom, rules, angle, iterations=1, length=8):
        self.axiom = axiom
        self.rules = rules
        self.iters = iterations
        self.angle = angle
        self.path = axiom

        self.t = turtle.Turtle()
        self.length = length

    def _generate_l_system(self):  # Создается L-система
        for _ in range(self.iters):
            for key, value in self.rules.items():
                """В пути, который изначально равен аксиоме заменяется каждый найденый """
                """символ (ключ) на соответствующее значение из словаря правил"""
                self.path = self.path.replace(key, value)

    def draw_turtle(self, length=8, size=2, start_pos=(0, 0), start_angle=0, width=600, height=600, ht=True):
        self._generate_l_system()

        wn = turtle.Screen()
        wn.setup(width, height)
        self.length = length
        self.t.pensize(size)

        turtle.tracer(1, 0)
        if ht:
            self.t.ht()
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()
        self._draw_l_system()
        turtle.done()

    def _draw_l_system(self):
        turtle_stack = []
        for move in self.path:
            if move == 'F':
                self.t.forward(self.length)
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)
            elif move == "[":
                turtle_stack.append((self.t.xcor(), self.t.ycor(), self.t.heading(), self.t.pensize()))
            elif move == "]":
                xcor, ycor, head, w = turtle_stack.pop()
                self.set_turtle((xcor, ycor, head))
                self.width = w
                self.t.pensize(self.width)
            elif move == "C":
                turtle.colormode(255)
                self.t.pencolor(randint(0, 255),
                                randint(0, 255),
                                randint(0, 255))

    def set_turtle(self, my_tuple):
        self.t.up()
        self.t.goto(my_tuple[0], my_tuple[1])
        self.t.seth(my_tuple[2])
        self.t.down()
