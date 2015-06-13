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
        self.min_distance = int(self.speed + 15)
        self.location = location
        self.following_who = following_who

    def __str__(self):
        return "{} {} {}".format(self.color, self.make, self.model, self.location, self.following_who)

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += 2
            return
        else:
            self.speed = self.following_who.speed
            return

    def decelerate(self):
        distraction = random.randint(0, 9)
        if distraction == 0:
            self.speed -= 2
            if self.speed < 0:
                self.speed = 0
            else:
                return
        else:
            return

    def simulation(self):
        for _ in range (5000):
            car_list = [car_1, car_2]
            prev_car_location = 1000
            for car in car_list:
                if prev_car_location > minimum_distance:
                    accelerate(self, car)
                    decelerate(self, car)
                    self.location += self.speed
                else:
                    decelerate(self, car)
                    self.location += self.speed
    simulation(self)







car_1 = Car("Hummer", "H1", "red", 25, "car_2")
car_2 = Car("Jeep", "Wrangler", "black", 5, "car_1")

print(car_1)
print("spd", car_1.speed)
print("loc", car_1.location)

print(car_2)
print("spd", car_2.speed)
print("loc", car_2.location)



print(car_1)
print("spd", car_1.speed)
print("loc", car_1.location)

print(car_2)
print("spd", car_2.speed)
print("loc", car_2.location)
