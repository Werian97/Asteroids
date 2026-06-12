import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from points import calculate_points, get_score
import sys



def main():
    pygame.init()
    pygame.mixer.init()
    points = pygame.font.SysFont("sans", 30)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.mixer.music.load("assets/sounds/space_sound.ogg")
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fart-steroid")
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

    destroyed = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH//2 , SCREEN_HEIGHT//2)
    asteroidfield = AsteroidField()
    running = True
    while running:
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
                running = False
        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split(destroyed)
        
        displayed_points = points.render("Points: " + str(calculate_points(destroyed)), True, "white")
        screen.blit(displayed_points, (30,0))

        pygame.display.flip()   
        dt = clock.tick(60) / 1000

    pygame.quit()
    print("Game over!")
    points = calculate_points(destroyed)
    print(f"You totalized {points} points")
    name = input("Enter your name: ")

    with open("classifica.txt", "r") as file:
        classifica = file.read()
    classifica_lines = classifica.split("\n")
    placement = 0
    for line in classifica_lines:
        if points <= get_score(line):
            placement += 1
        else:
            break
    point_line = f"{name}: {points}"
    new_classifica_lines = classifica_lines[0:placement]
    new_classifica_lines.append(point_line)
    new_classifica_lines.extend(classifica_lines[placement:len(classifica_lines)-1])
    new_classifica = "\n".join(new_classifica_lines)
    with open("classifica.txt", "w") as file:
        file.write(new_classifica)


if __name__ == "__main__":
    main()
