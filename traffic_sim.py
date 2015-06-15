import random

class Road:
    def __init__(self):
        self.length = 1000

    def __str__(self):
        return self.length


class Car:
    def __init__(self, location, following_who=None):
        self.speed = 0
        self.max_speed = 33
        self.min_distance = int(self.speed + 15)
        self.location = location
        self.following_who = following_who

    @property
    # wha?  So we use this to call without passing variables right?
    def __str__(self):
        return "{}".format(self.location)

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

    def simulate(self):
        if self.following_who.location > self.min_distance:
            self.accelerate()
            self.decelerate()
            self.location += self.speed
            if self.location >= road.length:
                self.location -= road.length
        else:
            self.decelerate()
            self.location += self.speed
            if self.location >= road.length:
                self.location -= road.length


road = Road()
car_list = []
location = 600
car_in_front = None
traffic = []
traffic_log = []
in_range = []
itteration_log = []
print(traffic_log)

for _ in range(30):
    # this creates the car instances
    car_to_spawn = Car(location, car_in_front)
    car_list.append(car_to_spawn)
    # this next line allows the first car to spawn without knowing who it is following by setting var above to none
    # Each iteration allows the first car to be assigned the last car no matter how many are put on the road
    car_list[0].following_who = car_list[-1]
    location -= 20
    car_in_front = car_to_spawn

print("DEBUG: first run")
for _ in range(60):
    print(_, " RUN")
    for car in car_list:
        car.simulate()
        [traffic.append(car.location)]
        [in_range.append(_)]
    [traffic_log.append(traffic)]
    # itteration log is for using with a scatter plot in homework
    itteration_log.append(in_range)
    traffic = []
    in_range = []
print(len(traffic_log[0]))
print(len(traffic_log))
print(traffic_log)