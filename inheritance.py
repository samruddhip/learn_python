class Car:
    @staticmethod
    def start():
        print("Car is starting")

    @staticmethod
    def stop():
        print("Car is stopping")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota("Corolla")
car2 = Toyota("Prius")

print(car1.start())  # Corolla

car1.start()