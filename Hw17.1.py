#exersise 1

class Rectangle:
    def __init__(self, l, w):
     self.length = l
     self.width = w

    def rectangle_area(self):
        return self.length * self.width
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())


#exersise 2

class Rocket:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y += 1
        print(self.y)
    def move_right(self):
        self.x += 1
        print(self.x)
    def mode_down(self):
        self.y -= 1
        print(self.y)
    def move_left(self):
        self.x -= 1
        print(self.x)
    def current_position(self):
        print(self.x, self.y)

Rocket = Rocket(0,0)
Rocket.move_up()
Rocket.move_right()
Rocket.move_left()
Rocket.mode_down()
Rocket.current_position()
