class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

ford.set_speed(300)
print(ford.get_speed())
print(ford.get_color())
