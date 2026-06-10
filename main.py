import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys



def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    player = Player(SCREEN_WIDTH//2 , SCREEN_HEIGHT//2)
    asteroidfield = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()   
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
