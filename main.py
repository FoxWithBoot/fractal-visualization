from LSystem2D import LSystem2D


def snowflake_koch():
    """Снежинка Коха"""
    axiom = "FC--FC--FC"
    rules = {"F": "F+F--F+F"}
    iterations = 3  # TOP: 7
    angle = 60
    ls = LSystem2D(axiom, rules, angle, iterations)
    ls.draw_turtle(start_pos=(-100, 100))


def vicek_fractal():
    """Фрактал Вичека"""
    axiom = "FC-FC-FC-FC"
    rules = {"F": "F-F+F+F-F"}
    iterations = 2  # TOP: 6
    angle = 90
    ls = LSystem2D(axiom, rules, angle, iterations)
    ls.draw_turtle(start_pos=(-100, 100), length=20)


def levy_curve():
    """Кривая Леви"""
    axiom = "F"
    rules = {"F": "+F--F+"}
    iterations = 8  # TOP: 16
    angle = 45
    ls = LSystem2D(axiom, rules, angle, iterations)
    ls.draw_turtle()


def sierpinski_lattice():
    """Решетка Серпинского"""
    axiom = "FXF--FF--FF"
    rules = {"F": "FF", "X": "--FXF++FXF++FXF--"}
    iterations = 5  # TOP: 8
    angle = 60
    ls = LSystem2D(axiom, rules, angle, iterations)
    ls.draw_turtle(start_pos=(-250, 250))


def anklets_of_krishna():
    """Анклеты Кришны"""
    axiom = " -XC--XC"
    rules = {"X": "XFX--XFX"}
    iterations = 1  # TOP: 9
    angle = 45
    ls = LSystem2D(axiom, rules, angle, iterations)
    ls.draw_turtle(start_pos=(-50, 100), length=20)


def pentaplexity():
    """Pentaplexity"""
    axiom = "F++F++F++F++F"
    rules = {"F": "F++F++F+++++F-F++F"}
    iterations = 2  # TOP: 5
    angle = 36
    ls = LSystem2D(axiom, rules, angle, iterations)
    ls.draw_turtle(start_pos=(-50, 0), length=20)


def tree():
    """Дерево"""
    axiom = "A"
    rules = {"F": "FF", "A": "F[+A][-A]"}
    iterations = 6  # TOP: 7
    angle = 33
    ls = LSystem2D(axiom, rules, angle, iterations)
    ls.draw_turtle(ht=False, start_angle=90, start_pos=(0, -300))


def branch():
    """Ветка"""
    axiom = "F"
    rules = {"F": "F[+F]F[-F]F"}
    iterations = 4  # TOP: 7
    angle = 25.7
    ls = LSystem2D(axiom, rules, angle, iterations)
    ls.draw_turtle(ht=False, start_angle=90, start_pos=(0, -300))


if __name__ == '__main__':
    #snowflake_koch()
    anklets_of_krishna()
    #pentaplexity()
    #vicek_fractal()
    #levy_curve()
    #sierpinski_lattice()
    #tree()
    #branch()



