from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
    
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        color = "white"
        points = self.triangle()
        pygame.draw.polygon(screen, color, points, LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0,1).rotate(self.rotation)
        movement = unit_vector * PLAYER_SPEED * dt
        self.position += movement
    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown <= 0:
                self.shoot()
                self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
                
    
    def shoot(self):
        shot = Shot(*self.position)
        unit_vector = pygame.Vector2(0,1).rotate(self.rotation)
        shot.velocity = PLAYER_SHOOT_SPEED * unit_vector

