#Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    title = None
    def draw(self):
        return "Запуск отрисовки"
class Pen(Stationery):
    def draw(self):
        return "Запуск отрисовки ручкой"
class Pencil(Stationery):
    def draw(self):
        return "Запуск отрисовки карандашом"
class Handle(Stationery):
    def draw(self):
        return "Запуск отрисовки маркером"
stat = Stationery()
print(stat.draw())
pen = Pen()
print(pen.draw())
pencil = Pencil()
print(pencil.draw())
handle = Handle()
print(handle.draw())