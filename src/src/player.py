import pygame
from config import PLAYER_SPEED, PLAYER_COLOR, PLAYER_RADIUS

class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.speed = PLAYER_SPEED
        self.radius = PLAYER_RADIUS
        self.color = PLAYER_COLOR
        self.loops = 0
        self.score = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_w]: dy -= 1
        if keys[pygame.K_s]: dy += 1
        if keys[pygame.K_a]: dx -= 1
        if keys[pygame.K_d]: dx += 1
        # normalize diagonal speed
        if dx and dy:
            dx *= 0.7071
            dy *= 0.7071
        self.x = max(self.radius, min(self.x + dx*self.speed, 800 - self.radius))
        self.y = max(self.radius, min(self.y + dy*self.speed, 600 - self.radius))

    def check_edge_and_reset(self):
        if (self.x <= self.radius or self.x >= 800 - self.radius or
            self.y <= self.radius or self.y >= 600 - self.radius):
            self.loops += 1
            self.x, self.y = 400, 300
            # scale difficulty
            self.speed += SPEED_INCREMENT
            return True
        return False
