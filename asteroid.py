from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.destruction_sound = pygame.mixer.Sound("assets/sounds/asteroid_destruction_sound.wav")
    
    def draw(self, screen):
        color = "white"
        center = self.position
        radius = self.radius
        width = LINE_WIDTH
        pygame.draw.circle(screen, color, center, radius, width)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        self.destruction_sound.play()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2
        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(*self.position, radius) # type: ignore
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(*self.position, radius) # type: ignore
        asteroid2.velocity = velocity2
