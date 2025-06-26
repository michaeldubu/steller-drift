import random
import pygame
from config import NUM_PLANETS, PLANET_COLOR, PLANET_MIN_SIZE, PLANET_MAX_SIZE

class Planet:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)
        self.size = random.randint(PLANET_MIN_SIZE, PLANET_MAX_SIZE)

    def draw(self, surface):
        pygame.draw.circle(surface, PLANET_COLOR, (self.x, self.y), self.size)

class PlanetManager:
    def __init__(self):
        self.planets = [Planet() for _ in range(NUM_PLANETS)]

    def regen(self):
        for p in self.planets:
            p.reset()

    def draw(self, surface):
        for p in self.planets:
            p.draw(surface)
