from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        color = "white"
        center = self.position
        radius = self.radius
        width = LINE_WIDTH
        pygame.draw.circle(screen, color, center, radius, width)
    
    def update(self, dt):
        self.position += self.velocity * dt