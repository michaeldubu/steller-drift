import random
import pygame
from config import NUM_STARS, STAR_COLOR, STAR_MIN_SIZE, STAR_MAX_SIZE

class Star:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.size = random.randint(STAR_MIN_SIZE, STAR_MAX_SIZE)

    def draw(self, surface):
        pygame.draw.circle(surface, STAR_COLOR, (self.x, self.y), self.size)

class StarField:
    def __init__(self):
        self.stars = [Star() for _ in range(NUM_STARS)]

    def regen(self):
        for star in self.stars:
            star.reset()

    def draw(self, surface):
        for star in self.stars:
            star.draw(surface)
