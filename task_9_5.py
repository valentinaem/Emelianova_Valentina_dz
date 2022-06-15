# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка синими чернилами')
class Pencil(Stationery):
    def draw(self):
        print('Отрисовка тонкой линией')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка жирной линией')

pen_1 = Pencil('kon-i-noor')
pen_1.draw()
pen_2 = Handle('ProMarker')
pen_2.draw()