import random, math
import pygame
from config import NUM_EVENTS, EVENT_COLOR, EVENT_RADIUS, EVENT_TYPES

class Event:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.radius = EVENT_RADIUS
        self.type = random.choice(EVENT_TYPES)
        self.color = EVENT_COLOR
        self.triggered = False

    def draw(self, surface):
        if not self.triggered:
            pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def check_trigger(self, player):
        dist = math.hypot(self.x - player.x, self.y - player.y)
        if dist < self.radius + player.radius and not self.triggered:
            self.triggered = True
            return self.type
        return None

class EventManager:
    def __init__(self):
        self.events = [Event() for _ in range(NUM_EVENTS)]

    def regen(self):
        self.events = [Event() for _ in range(NUM_EVENTS)]

    def draw(self, surface):
        for e in self.events:
            e.draw(surface)

    def update(self, player):
        triggered = []
        for e in self.events:
            result = e.check_trigger(player)
            if result:
                triggered.append(result)
        return triggered
