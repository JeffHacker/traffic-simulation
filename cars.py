import random

class Car:
    def __init__(self, make, model, color):
        self.color = color
        self.make = make
        self. model = model
        self.speed = 0
        self.moving = False
        self.safe_driver = True
        self.accelerate = False

    def __str__(self):
        return "{} {} {}".format(self.color, self.make, self.model)


car_1 = Car("Hummer", "H1", "red")
car_2 = Car("Jeep", "Wrangler", "black")
car_3 = Car("VW", "Jetta", "white")
car_4 = Car("Jeep", "Cherokee", "green")
car_5 = Car("Isuzu", "Rodeo", "red")
car_6 = Car("Mitsubishi", "Lancer", "Aqua")
car_7 = Car("Ford", "Festiva", "baby blue")
car_8 = Car("Hyundai", "Elantra", "dark blue")
car_9 = Car("Lincoln", "Towncar", "light blue")
car_10 = Car("Ford", "Mustang", "red")
car_11 = Car("Chevy", "Impala", "tan")
car_12 = Car("Ford", "Fairmont", "green")
car_13 = Car("Dodge", "minivan", "plum")
car_14 = Car("Chevy", "pickup", "green")
car_15 = Car("Ford", "Taurus", "green")
car_16 = Car("Ford", "Escrort", "red")
car_17 = Car("Icon", "CJ", "grey")
car_18 = Car("Mack", "dump truck", "white")
car_19 = Car("Dodge", "Ram", "silver")
car_20 = Car("Chevy", "dually", "gold")
# need 10 more cars but it's a good start

# random just for fun and may use somehow for homework
x = random.randint(0,19)

car_list = [car_1, car_2, car_3, car_4, car_5, car_6, car_7, car_8, car_9, car_10, car_11, car_12, car_13, car_14,
            car_15, car_16, car_17, car_18, car_19, car_20]
print(car_list[x])






