#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car():
    speed = None
    color = None
    name = None
    is_police = None

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Машина двигается"

    def stop(self):
        return "Машина остановилась"

    def direction(self, direction):
        self.direction = direction
        return (f"Машина повернула {direction}")

    def show_speed(self):
        return (f"Скорость машины : {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return ("Вы превысели скоростной режим")
        else:
            return (f"Ваша скорость составляет - {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return ("Ваша машина превышает скоростной режим")
        else:
            return (f"Ваша скорость составляет - {self.speed}")


town_car = TownCar(70, 'Green', 'KIA', 'Fales')
police_car = PoliceCar(100, 'Blue', 'Ford', 'True')
work_car = WorkCar(50, 'Black', 'Lada', 'False')
sport_car = SportCar(120, 'White', 'Porsche', 'False')
print(town_car.speed, town_car.color, town_car.name, town_car.is_police)
print(police_car.speed, police_car.color, police_car.name, police_car.is_police)
print(work_car.speed, work_car.color, work_car.name, work_car.is_police)
print(sport_car.speed, sport_car.color, sport_car.name, sport_car.is_police)

print(police_car.go(), police_car.stop(), police_car.direction("направо"), police_car.show_speed())
print(town_car.go(), town_car.stop(), town_car.direction("налево"), town_car.show_speed())
print(work_car.go(), work_car.stop(), work_car.direction("в обратном направлении"), work_car.show_speed())
print(sport_car.go(), sport_car.stop(), sport_car.direction("назад"), sport_car.show_speed())