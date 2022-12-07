#exersise 1

class Rectangle:
    lenght = 10
    width = 20
    area=(lenght * width)

area_of_rec=Rectangle
print(area_of_rec.area)


#exersise 2

class Rocket:

    def __int__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y = +1

    def move_right(self):
        self.x = +1

    def mode_down(self):
        self.y = -1

    def move_left(self):
        self.x = -1

    def current_position(self):


print(self.x)
print(self.y)