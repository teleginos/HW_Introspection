import inspect



def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None
    info['method'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]

    return info


class Car:
    def __init__(self, make, model, year, color):
        self.make = make  # Производитель автомобиля
        self.model = model  # Модель автомобиля
        self.year = year  # Год выпуска
        self.color = color  # Цвет автомобиля

    def start(self):
        return f"{self.make} {self.model} заведен!"

    def stop(self):
        return f"{self.make} {self.model} остановлен!"

    def paint(self, new_color):
        old_color = self.color
        self.color = new_color
        return f"Цвет {self.make} {self.model} изменен с {old_color} на {new_color}."

    def info(self):
        return f"Автомобиль: {self.year} {self.make} {self.model}, цвет: {self.color}"


number = 42
sentence = 'Hello, world!'
my_car = Car("Toyota", "Camry", 2020, "синий")

print(f"Запуск функции с переменной number\n{introspection_info(number)}")
print(f"\nЗапуск функции с переменной sentence\n{introspection_info(sentence)}")
print(f"\nЗапуск функции с объектом класса Car\n{introspection_info(my_car)}")
