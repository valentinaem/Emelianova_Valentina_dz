# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.direction = direction

    def go(self):
        print(f'{self.name} поехала')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn(self):
        print(f'{self.name} едет {self.direction}')
    def show_speed(self):
        print(f'скорость {self.speed}')
    def it_is(self):
        if self.is_police == True:
            print('It is police car')
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
    def it_is(self):
        print('It is town car')
class SportCar(Car):
    def it_is(self):
        print('It is sport car')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
    def it_is(self):
        print('It is work car')
class PoliceCar(Car):
    def qwe(self):
        print('qwe')

car_1 = TownCar(65, 'black', 'volvo', False, 'налево')
car_1.go()
car_1.turn()
car_1.show_speed()
car_2 = PoliceCar(45, 'blue', 'mazda', True, 'направо')
car_2.show_speed()
car_2.it_is()

