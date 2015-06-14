import random

class Road:
    def __init__(self):
        self.length = 1000

    def __str__(self):
        return self.length


class Car:
    def __init__(self, make, model, color, location, following_who):
        self.color = color
        self.make = make
        self.model = model
        self.size = 15
        # speed in m/s
        self.speed = 10
        self.max_speed = 33
        self.safe_driver = True
        self.min_distance = self.speed + 15
        self.location = location
        self.following_who = following_who

    def __str__(self):
        return "{} {} {}".format(self.color, self.make, self.model, self.location, self.following_who)

    def decelerate(self):
        distraction = random.randint(0, 9)
        if distraction == 0:
            # speed in m/s
            if self.speed <= 0:
                self.speed = 0
            else:
                self.speed -= 2
        else:
            return

    def accelerate(self):
        if self.following_who.location >= self.min_distance:
            self.speed += 2
        else:
            return





car_1 = Car("Hummer", "H1", "red", 580, "car_30")
car_2 = Car("Jeep", "Wrangler", "black", 560, "car_1")
car_3 = Car("VW", "Jetta", "white", 540, "car_2")
car_4 = Car("Jeep", "Cherokee", "green", 520, "car_3")
car_5 = Car("Isuzu", "Rodeo", "red", 500, "car_4")
car_6 = Car("Mitsubishi", "Lancer", "Aqua", 480, "car_5")
car_7 = Car("Ford", "Festiva", "baby blue", 460, "car_6")
car_8 = Car("Hyundai", "Elantra", "dark blue", 440, "car_7")
car_9 = Car("Lincoln", "Towncar", "light blue", 420, "car_8")
car_10 = Car("Ford", "Mustang", "red", 400, "car_9")
car_11 = Car("Chevy", "Impala", "tan", 380, "car_10")
car_12 = Car("Ford", "Fairmont", "green", 360, "car_11")
car_13 = Car("Dodge", "minivan", "plum", 340, "car_12")
car_14 = Car("Chevy", "pickup", "green", 320, "car_13")
car_15 = Car("Ford", "Taurus", "green", 300, "car_14")
car_16 = Car("Ford", "Escrort", "red", 280, "car_15")
car_17 = Car("Icon", "CJ", "grey", 260, "car_16")
car_18 = Car("Mack", "dump truck", "white", 240, "car_17")
car_19 = Car("Dodge", "Ram", "silver", 220, "car_18")
car_20 = Car("Chevy", "dually", "gold", 200, "car_19")
car_21 = Car("Mazda", "mini truck", "rusty, brown", 180, "car_20")
car_22 = Car("Chevy", "Chevette", "tan", 160, "car_21")
car_23 = Car("Datsun", "B210", "red", 140, "car_22")
car_24 = Car("Ford", "pickup", "black", 120, "car_23")
car_25 = Car("AMC", "Pacer", "white", 100, "car_24")
car_26 = Car("Jeep", "CJ7", "red", 80, "car_25")
car_27 = Car("Honda", "Accord", "white", 60, "car_26")
car_28 = Car("Chevy", "Nova", "bronze", 40, "car_27")
car_29 = Car("Wayne Ind.", "Batmobile", "black", 20, "car_28")
car_30 = Car("home-made", "motorized lawnchair", "ducktaped", 0, "car_29")


car_list = [car_1, car_2, car_3, car_4, car_5, car_6, car_7, car_8, car_9, car_10, car_11, car_12, car_13, car_14,
            car_15, car_16, car_17, car_18, car_19, car_20, car_21, car_22, car_23, car_24, car_25, car_26, car_27,
            car_28, car_29, car_30]

# random just for fun and may use somehow for homework
x = random.randint(0, 29)

print(car_list[x])

print(car_1.speed)

car_1.decelerate()

print(car_1.speed)

# car_1.accelerate()

print(car_1.speed)