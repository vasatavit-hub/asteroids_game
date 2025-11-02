from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, position, rotation):
        super().__init__(position.x, position.y,SHOT_RADIUS)
        direction = pygame.Vector2(0,1)
        self.velocity = direction.rotate(rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, screen):
        pygame.draw.circle (screen, (255,255,255), self.position,self.radius, 2)