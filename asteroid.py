from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        color = "white"
        center = self.position
        radius = self.radius
        width = LINE_WIDTH
        pygame.draw.circle(screen, color, center, radius, width)
    
    def update(self, dt):
        self.position += self.velocity * dt
