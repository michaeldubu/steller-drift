import pygame
import sys
from config import WIDTH, HEIGHT, FPS, LOOPS_BEFORE_HARD
from player import Player
from starfield import StarField
from planet_manager import PlanetManager
from event_manager import EventManager

def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Stellar Drift – Infinite Loop")
    clock = pygame.time.Clock()

    player = Player(WIDTH//2, HEIGHT//2)
    stars = StarField()
    planets = PlanetManager()
    events = EventManager()

    font = pygame.font.SysFont(None, 24)

    running = True
    while running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Edge loop
        if player.check_edge_and_reset():
            stars.regen()
            planets.regen()
            events.regen()

        # Event checks
        for e_type in events.update(player):
            print(f"Event: {e_type}")
            # simple scoring: +10 for resource, -15 for black hole
            if e_type == "Resource Discovery":
                player.score += 10
            elif e_type == "Black Hole":
                player.score = max(0, player.score - 15)
            else:
                player.score += 5

        # DRAW
        screen.fill((0, 0, 0))
        stars.draw(screen)
        planets.draw(screen)
        events.draw(screen)
        player.draw(screen)

        # HUD
        hud = font.render(
            f"Score: {player.score}   Loops: {player.loops}", True, (200,200,200)
        )
        screen.blit(hud, (10,10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
