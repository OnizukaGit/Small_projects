from random import randint


class Rocket:
    def __init__(self, speed):
        self.altitude = 0
        self.speed = speed

    def moveUp(self):
        if self.speed:
            self.altitude += self.speed


rockets = [Rocket(4) for _ in range(5)]

for _ in range(10):
    rocketsIndexToMove = randint(0, 4)
    rockets[rocketsIndexToMove].moveUp()

for i,rocket in enumerate(rockets):
    print(f"Prędkość rakiety {i + 1}:", rocket.altitude, "km/s")

